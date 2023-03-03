"""Python imports"""
from websockets import ConnectionClosed
from json import loads

"""Source imports"""
from SocketServer.WebSocketServer import WebSocketServer
from DB.DBSession import DBSession
from Utils.Utils import *

CLASS_NAME = 'ThirdPartServer'

class ThirdPartServer(WebSocketServer):
    def __init__(self, maindirectory):

        super().__init__(maindirectory)
        self.__EventWriter = None
        self.__clients     = {}
        self.__db          = None

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

    def connect_db_session(self, maindirectory):
        config      = read_config_db_file(maindirectory+'../..')
        login       = config['login']
        password    = config['password']
        ip          = config['ip']
        port        = config['port']

        self.__db   = DBSession(login, password, ip, port)
        self.__db.start_db_session()

if __name__=='__main__':
    maindirectory = get_main_directory()
    ThPartServer = ThirdPartServer(maindirectory)
    ThPartServer.__EventWriter = start_log(CLASS_NAME)
    ThPartServer.connect_db_session(maindirectory)
    ThPartServer.__startServer__(ThPartServer.__msg_handler__, 3001)