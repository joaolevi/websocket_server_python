#!/usr/bin/env python

import websockets
from asyncio import create_task, Queue
from json import loads

from ..server import WebSocketServer

CLASS_NAME = 'ClientAccess'
REQ_CLIENT_LOGIN = 1

class ClientAccess(WebSocketServer):
    def __init__(self, accessconfig, maindirectory):
        """Initialize class and variables

            Args:
                accessconfig ([Dict]): [access config file content]
                maindirectory ([String]): [main directory]
        """
        super().__init__(accessconfig, maindirectory)

        self.__clients          = {}

    async def __msg_handler__(self, websocket, path):
        """
        A handle function to websocket handles.
        Login requests from Hades will create a new Client thread 
        with a queue as communication channel between threads.

        Args:
            websocket: used to sent menssages to client (Hades)
        """
        self.__EventWriter.write_msg(CLASS_NAME+'.msg_handler: client is sending a request...')
        while True: 
            try:
                data = await websocket.recv()
                json_hades_msg = loads(data)

                request_type = json_hades_msg['e']
                user = json_hades_msg['user']

                if request_type == REQ_CLIENT_LOGIN:
                    if not(user in self.__clients):
                        out_queue = Queue()

                        Client = Client(self.__accessconfig, self.__maindirectory, websocket, self.__EventWriter)

                        self.__clients[user] = {}
                        self.__clients[user]['task'] = create_task(Client.client_msg_handler(out_queue))
                        self.__clients[user]['queue'] = out_queue
                        await self.__clients[user]['queue'].put(data)
                    else:
                        continue
                else:
                    await self.__clients[user]['queue'].put(data)

            except websockets.ConnectionClosed:
                print(CLASS_NAME+' : '+'Terminated')
                break
            except Exception as e:
                print(CLASS_NAME+'.__msg_handler__: '+str(e))

    def start(self):
        """Start logs"""
        print('Starting...')