#!/usr/bin/env python
from json import loads
from asyncio import (create_task, wait_for, CancelledError, TimeoutError)
from websockets import connect

HOST = '127.0.0.1:3001'

CLASS_NAME = 'SocketClient'

class SocketClient():
    def __init__(self, websocket, EventWriter):
        self.__consume_task    = None
        self.__th_part_server  = None
        self.__main_server     = websocket
        self.__EventWriter     = EventWriter

    async def start_server_connection(self, data):
        async with connect('ws://'+HOST) as self.ServerConnection:
            await self.ServerConnection.send(data)
            response = await self.ServerConnection.recv()
            self.EventWriter.debug(response)

    async def __connect_ws__(self):
        ws = await connect('ws://'+HOST)
        return(ws)

    async def start_connection(self):
        self.main_server = await self.__connect_ws__()

    async def client_msg_handler(self, input_queue):
        while True:
            data = await input_queue.get()
            self.__EventWriter.debug(CLASS_NAME+'.client_msg_handler: Msg='+data)
            try:
                json_msg = loads(data)
                request_number = json_msg['e']
                if (request_number == 1):
                    await self.start_connection()
                    await self.main_server.send(data)

            except Exception as e:
                self.__EventWriter.write_error(str(e))
                        
            input_queue.task_done()

