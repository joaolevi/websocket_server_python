"""Python imports"""
from websockets import ConnectionClosed
from json import loads

"""Source imports"""
from SocketServer.WebSocketServer import WebSocketServer
from DB.DBSession import DBSession
from Utils.Utils import *
from DB.DBDataTypes import *

CLASS_NAME = 'ThirdPartServer'
DB_TYPE_CLIENT     = 1
DB_TYPE_STUDENT    = 2

class ThirdPartServer(WebSocketServer):
    def __init__(self, maindirectory):

        super().__init__(maindirectory)
        self.EventWriter = None
        self.__clients     = {}
        self.__db          = None

    async def __msg_handler__(self, websocket, path):
        self.EventWriter.debug(CLASS_NAME+'.msg_handler: client is sending a request...')
        while True: 
            try:
                data = await websocket.recv()
                json_msg = loads(data)
                
                db_data = None
                dbtype = json_msg['db_type']
                if (dbtype == DB_TYPE_CLIENT):
                    db_data = self.create_client(json_msg)
                elif (dbtype == DB_TYPE_STUDENT):
                    db_data = self.create_student(json_msg)

                self.__db.save_to_db(db_data) 

                self.EventWriter.debug(CLASS_NAME+'.msg_handler')

            except ConnectionClosed:
                print(CLASS_NAME+' : '+'Terminated')
                break
            except Exception as e:
                print(CLASS_NAME+'.__msg_handler__: '+str(e))

    def connect_db_session(self, maindirectory):
        config   = read_config_db_file(maindirectory+'../..')
        login    = config['login']
        password = config['password']
        ip       = config['ip']
        port     = config['port']

        self.__db   = DBSession(login, password, ip, port)
        self.__db.start_db_session()

    def create_client(self, json_msg):
        name = json_msg['name']
        age  = json_msg['age']
        cpf  = json_msg['cpf']
        return(ClientDB(name=name, age=age, cpf=cpf))
        
    def create_student(self, json_msg):
        name = json_msg['name']
        msg  = json_msg['msg']
        return(Student(name=name, msg=msg))
    
    def start_log(self):
        basicConfig(filename="./log/EventThPartServer.log", format='%(asctime)s %(message)s', filemode='w')
        self.EventWriter = getLogger()
        self.EventWriter.setLevel(DEBUG)

if __name__=='__main__':
    maindirectory = get_main_directory()
    ThPartServer = ThirdPartServer(maindirectory)
    ThPartServer.start_log()
    ThPartServer.connect_db_session(maindirectory)
    ThPartServer.__startServer__(ThPartServer.__msg_handler__, 3001)