from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://joaolevi:1234@localhost:5432/postgres', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class ClientDB(Base):
    __tablename__ = 'client_db'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    cpf = Column(String(50))

Base.metadata.create_all(engine)