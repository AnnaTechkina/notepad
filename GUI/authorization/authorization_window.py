from tkinter import *
from GUI.templates import BaseInputWindow


# ПРИ НАЖАТИИ АВТОРИЗАЦИЯ
class AuthorizationWindow(BaseInputWindow):
    def __init__(self):
        super().__init__("АВТОРИЗАЦИЯ", "600x800")

        self.__login_but = Button(self,
                                  width=15,
                                  text='ВОЙТИ',
                                  relief=SOLID,
                                  cursor='hand2',
                                  font=('Arial', 10),
                                  command=None)
        self.__login_but.pack(pady=15)
