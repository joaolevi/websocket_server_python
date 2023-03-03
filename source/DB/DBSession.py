from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

class DBSession():
    def __init__(self, login, password, ip, port):
        self.session         = None
        self.__login         = login
        self.__password      = password
        self.__ip            = ip
        self.__port          = port
    
    def start_db_session(self):
        engine = create_engine('postgresql://'+self.__login+':'+self.__password+'@'+self.__ip+':'+self.__port+'/postgres')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        Base = declarative_base()
        Base.metadata.create_all(engine)

    def save_to_db(self, data):
        if (self.session.connection()):
            self.session.add(data)
            self.session.commit()
        else:
            self.start_db_session()