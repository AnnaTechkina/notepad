#from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
#from sqlalchemy import Column, Integer, String, Engine
from sqlalchemy import *



class _Base(DeclarativeBase): pass

class Users(_Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, index=True, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

class Files(_Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, autoincrement=True)
    path = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, unique=True, index=True, nullable=False)
    salt = Column(String, nullable=False)
    nonce = Column(String, nullable=False)
    tag = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

def create_tables(engine: Engine):
    _Base.metadata.create_all(engine)

