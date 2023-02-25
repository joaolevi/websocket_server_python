#!/usr/bin/env python
from json import loads
from asyncio import (create_task, wait_for, CancelledError, TimeoutError)

TIME_OUT_WAITING_MSG = 5
TIME_TO_TRY_CONNECTION = 10
VERIFIER_SLEEP_TIMER = 10

CLASS_NAME = 'SocketClient'

class SocketClient():
    def __init__(self, websocket, EventWriter):
        self.__consume_task = None
        self.__serverws     = websocket
        self.__EventWriter  = EventWriter

    async def client_msg_handler(self, input_queue):
        while True:
            data = await input_queue.get()
            self.__EventWriter.debug(CLASS_NAME+'.client_msg_handler: Msg='+data)
            try:
                msg = loads(data)
                self.__EventWriter.debug(CLASS_NAME+'.client_msg_handler: msg from client: '+msg)

            except Exception as e:
                self.__EventWriter.write_error(str(e))
                        
            input_queue.task_done()

