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

    async def consume(self):
        await self.send_heartbeat()

        msg_buf = bytearray()
        while True:
            try:
                msg_buf = await wait_for(self.brokerws.recv(), timeout=TIME_OUT_WAITING_MSG)

            except TimeoutError:
                if self.brokerws.open:
                    await self.send_heartbeat()
                else:
                    return
            except Exception as e:
                print(CLASS_NAME+".consume: "+str(e))


    async def client_msg_handler(self, input_queue):
        while True:
            data = await input_queue.get()
            try:
                msg = loads(data)
                print(CLASS_NAME+'.client_msg_handler: msg from client: '+msg)

            except Exception as e:
                self.__EventWriter.write_error(str(e))
                        
            input_queue.task_done()

