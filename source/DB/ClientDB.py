from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class ClientDB(Base):
    __tablename__ = 'client_db'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    cpf = Column(String(50))

# Base.metadata.create_all(engine)

client1 = ClientDB(name='John Rich', age=26, cpf='999.000.111-89')
client2 = ClientDB(name='Mariana Raujo', age=28, cpf='222.030.113-52')
client3 = ClientDB(name='Piter Parker', age=25, cpf='311.232.456-64')

session.add(client1)

session.add_all([client2, client3])

session.commit()