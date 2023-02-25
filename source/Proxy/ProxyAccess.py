#!/usr/bin/env python

"""Imports"""
import websockets
from asyncio import create_task, Queue
from json import loads

"""Source imports"""
from ..SocketServer.WebSocketServer import WebSocketServer
from ..SocketClient.SocketClient import SocketClient

CLASS_NAME = 'ProxyAccess'
REQ_CLIENT_LOGIN = 1

class ProxyAccess(WebSocketServer):
    def __init__(self, maindirectory, EventWriter):

        super().__init__(maindirectory)
        self.__EventWriter = EventWriter
        self.__clients = {}

    async def __msg_handler__(self, websocket, path):
        self.__EventWriter.debug(CLASS_NAME+'.msg_handler: client is sending a request...')
        while True: 
            try:
                data = await websocket.recv()
                json_msg = loads(data)

                request_type = int(json_msg['e'])
                user = json_msg['user']

                self.__EventWriter.debug(CLASS_NAME+'.msg_handler: Req='+str(request_type)+'; User='+user)

                if request_type == REQ_CLIENT_LOGIN:
                    if not(user in self.__clients):
                        out_queue = Queue()

                        Client = SocketClient(websocket, self.__EventWriter)
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