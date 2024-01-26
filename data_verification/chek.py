from sqlalchemy import select
from sqlalchemy.orm import Session

from database.tables import Users, Files
from database.connecting_db import engine

def check_existence_file(filename: str):
    with Session(bind=engine) as session:
        query = select(Files.name).where(Files.name == filename)
        result = session.execute(query).one_or_none()
        return bool(result)

def check_existence_login(**kwargs):
    session = Session(bind=engine)
    query = select(Users).where(Users.login == kwargs['login'])
    result = session.execute(query)
    print(result)


def check_password_chars(**kwargs):
    password = kwargs['password']
    forbidden_char = " _#@?,.<>[]{}'/\\|\"=+-)(*&^:;`~"
    for char in forbidden_char:
        if char in password:
            print('Пароль содержит запрещенные символы')


def check_login_chars(**kwargs):
    login = kwargs['login']
    forbidden_char = " #@?,.<>[]{}'/\\|\"=+-)(*&^:;`~"
    for char in forbidden_char:
        if char in login:
            print('Логин содержит запрещенные символы')