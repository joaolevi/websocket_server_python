from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from enum import Enum

class DatabaseTypes(Enum):
    CLIENT  = 1
    STUDENT = 2

Base = declarative_base()

class ClientDB(Base):
    __tablename__ = 'client_db'

    id      = Column(Integer, primary_key=True)
    name    = Column(String(50))
    age     = Column(Integer)
    cpf     = Column(String(50))
    db_type = Column(Integer)

class Student(Base):
    __tablename__ = 'students'

    id      = Column(Integer, primary_key=True)
    name    = Column(String(50))
    msg     = Column(String(50))
    db_type = Column(Integer)


# Base.metadata.create_all(engine)

# client1 = ClientDB(name='John Rich', age=26, cpf='999.000.111-89')
# client2 = ClientDB(name='Mariana Raujo', age=28, cpf='222.030.113-52')
# client3 = ClientDB(name='Piter Parker', age=25, cpf='311.232.456-64')

# session.add(client1)

# session.add_all([client2, client3])

# session.commit()

###############
## Get all data

# clients = session.query(ClientDB)

# for client in clients:
#     print(client.name, client.age, client.cpf)

####################
## Get data in order

# clients = session.query(ClientDB).order_by(ClientDB.name)

# for client in clients:
#     print(client.name)

########################
## Get data by filtering

# clients = session.query(ClientDB).filter(ClientDB.name=="John Rich")

# for client in clients:
#     print(client.name, client.age)