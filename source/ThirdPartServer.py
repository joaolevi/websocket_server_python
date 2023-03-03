"""Python imports"""
from websockets import ConnectionClosed
from json import loads

"""Source imports"""
from SocketServer.WebSocketServer import WebSocketServer
from DB.DBSession import DBSession
from Utils.Utils import *
from DB.DBDataTypes import *

CLASS_NAME = 'ThirdPartServer'

class ThirdPartServer(WebSocketServer):
    def __init__(self, maindirectory):

        super().__init__(maindirectory)
        self.__EventWriter = None
        self.__clients     = {}
        self.__db          = None
        self.__dbtypes     = DatabaseTypes()

    async def __msg_handler__(self, websocket, path):
        while True: 
            try:
                data = await websocket.recv()
                json_msg = loads(data)

                dbtype = json_msg['db_type']
                if (dbtype == self.__dbtypes.CLIENT):
                    db_data = self.create_client(json_msg)
                elif (dbtype == self.__dbtypes.STUDENT):
                    db_data = self.create_student(json_msg)

                self.__db.save_to_db(db_data) 

                self.__EventWriter.debug(CLASS_NAME+'.msg_handler')

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

    def create_client(self, json_msg):
        id   = json_msg['id']
        name = json_msg['name']
        age  = json_msg['age']
        cpf  = json_msg['cpf']
        return(ClientDB(id=id, name=name, age=age, cpf=cpf, db_type=self.__dbtypes.CLIENT))
        
    def create_student(self, json_msg):
        id   = json_msg['id']
        name = json_msg['name']
        msg  = json_msg['msg']
        return(Student(id=id, name=name, msg=msg, db_type=self.__dbtypes.STUDENT))

if __name__=='__main__':
    maindirectory = get_main_directory()
    ThPartServer = ThirdPartServer(maindirectory)
    ThPartServer.__EventWriter = start_log(CLASS_NAME)
    ThPartServer.connect_db_session(maindirectory)
    ThPartServer.__startServer__(ThPartServer.__msg_handler__, 3001)