# Websocket Server in Python
This is an app built in python using Websockets and concepts like threads and coroutines

### Creating a table on PostgreSQL

To create a table I used SQLAlchemy. The table name is 'client_db' and it has these attributes:

```
class ClientDB(Base):
    __tablename__ = 'client_db'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    cpf = Column(String(50))
```

To access the tables in WSL we can open the psql Shell using `sudo -u postgres psql`.

To see the databases use this command on the Shell `\l`

I have the default databases and a database named `dummy`. To this project I used de default `postgres`

![image](https://user-images.githubusercontent.com/56874672/222305440-61b9b050-425a-4884-a33f-95983ea8321c.png)

After running the source/DB/ClientDB.py, we can see that the table was created using the command `\c postgres` to connect with the postgres database, and `\dt` to list the relations:

![image](https://user-images.githubusercontent.com/56874672/222305612-234ab8b0-2daf-45a4-ac53-100f18828af7.png)

## Client Window

This window was created using the Tkinter library on Python. The main idea is just to have a way where we can write some pieces of information and send to the database using our proxy system. 

![image](https://user-images.githubusercontent.com/56874672/222796220-c5c474e1-58c8-4867-b41e-698c27ede86d.png)
