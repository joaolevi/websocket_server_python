#!/usr/bin/env python

import websockets
from asyncio import create_task, Queue
from json import loads

from ..server.WebSocketServer import WebSocketServer
from ..client.SocketClient import SocketClient

CLASS_NAME = 'ProxyAccess'
REQ_CLIENT_LOGIN = 1

class ProxyAccess(WebSocketServer):
    def __init__(self, accessconfig, maindirectory):
        super().__init__(accessconfig, maindirectory)

        self.__clients = {}

    async def __msg_handler__(self, websocket, path):
        print(CLASS_NAME+'.msg_handler: client is sending a request...')
        while True: 
            try:
                data = await websocket.recv()
                json_msg = loads(data)

                request_type = json_msg['e']
                user = json_msg['user']

                if request_type == REQ_CLIENT_LOGIN:
                    if not(user in self.__clients):
                        out_queue = Queue()

                        Client = SocketClient(self.__accessconfig, self.__maindirectory, websocket, self.__EventWriter)

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
        print('Starting...')