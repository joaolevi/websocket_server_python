CLASS_NAME = 'ClientAccess'

from websockets import connect
from os import path
from inspect import getfile, currentframe
from logging import basicConfig, getLogger, DEBUG
from asyncio import get_event_loop

HOST = '127.0.0.1:3000'

class ClientAccess():
    def __init__(self):
        self.ServerConnection = None
        self.EventWriter      = None
        self.maindirectory    = ''

    def get_main_directory(self):
        self.maindirectory = path.dirname(path.abspath(getfile(currentframe())))

    def start_log(self):
        basicConfig(filename="../log/EventClientAccess.log", format='%(asctime)s %(message)s', filemode='w')
        self.EventWriter = getLogger()
        self.EventWriter.setLevel(DEBUG)

    async def start_server_connection(self):
        async with connect('ws://'+HOST) as self.ServerConnection:
            jsonMsg = '{"e":"1", "user":"joaolevi", "msg":"Primeira mensagem"}'
            await self.ServerConnection.send(jsonMsg)
            response = await self.ServerConnection.recv()
            self.EventWriter.debug(response)
 
if __name__ == "__main__":
    Client = ClientAccess()
    Client.get_main_directory()
    Client.start_log()
    get_event_loop().run_until_complete(Client.start_server_connection())
    