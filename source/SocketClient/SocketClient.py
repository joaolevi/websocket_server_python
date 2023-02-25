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

    async def start_server_connection(self):
        async with connect('ws://'+HOST) as self.ServerConnection:
            await self.ServerConnection.send(jsonMsg)
            response = await self.ServerConnection.recv()
            self.EventWriter.debug(response)

    async def client_msg_handler(self, input_queue):
        while True:
            data = await input_queue.get()
            self.__EventWriter.debug(CLASS_NAME+'.client_msg_handler: Msg='+data)
            try:
                json_msg = loads(data)
                request_number = json_msg['e']
                if (request_number == 1):
                    

            except Exception as e:
                self.__EventWriter.write_error(str(e))
                        
            input_queue.task_done()

