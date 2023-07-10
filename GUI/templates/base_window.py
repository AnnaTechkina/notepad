from typing import List
from tkinter import Tk

from GUI.templates import InputForm


class BaseWindow(Tk):
    def __init__(self, title: str, geometry: str):
        super().__init__()
        self.title(title)
        self.geometry(geometry)


class BaseInputWindow(BaseWindow):
    def __init__(self, title: str, geometry: str):
        super().__init__(title, geometry)

        self.__login_form = InputForm(self, 'ЛОГИН', 30)
        self.__login_form.pack(pady=15)

        self.__password_form = InputForm(self, 'ПАРОЛЬ', 30, show='*')
        self.__password_form.pack(pady=15)

    def get(self) -> List[str]:
        return [self.__login_form.get(), self.__password_form.get()]
