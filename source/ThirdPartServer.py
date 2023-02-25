from websockets import ConnectionClosed
from json import loads

from .SocketServer.WebSocketServer import WebSocketServer


CLASS_NAME = 'ThirdPartServer'

class ThirdPartServer(WebSocketServer):
    def __init__(self, maindirectory):

        super().__init__(maindirectory)
        self.__EventWriter = None
        self.__clients     = {}

    async def __msg_handler__(self, websocket, path):
        while True: 
            try:
                data = await websocket.recv()
                json_msg = loads(data)

                user_id = json_msg['userID']
                client_msg = json_msg['msg']

                if (not self.__clients.has_key(user_id)):
                    self.__clients[user_id] = []
                
                self.__clients[user_id].append(client_msg)

                self.__EventWriter.debug(CLASS_NAME+'.msg_handler: UserID=' + user_id + '; Msg='+ client_msg)

            except ConnectionClosed:
                print(CLASS_NAME+' : '+'Terminated')
                break
            except Exception as e:
                print(CLASS_NAME+'.__msg_handler__: '+str(e))