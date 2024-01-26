from typing import Optional, Sequence
from os.path import abspath

from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import Session

from database.tables import Users, Files
from database.connecting_db import engine
from data_verification.chek import check_existence_file

def creat_users(user: Users, id: int, login: str):
    pass





def get_filenames(user: Users):
    session = Session(bind=engine)
    query = select([Files.name]).where(Files.user_id == user.id)
    result = session.execute(query)
    return result.fetchall()

def create_file(user: Users, filename: str):
    if check_existence_file(filename):
        return False
    try:
        with open(abspath(filename), 'w', encoding='utf-8'):
            session = Session(bind=engine)
            query = insert(Files).values(path=filename, user_id=user.id)
            session.execute(query)
        return True
    except Exception as e:
        print(e)
        return False