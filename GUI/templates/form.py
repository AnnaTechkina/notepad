from tkinter import *


class InputForm(Frame):

    def __init__(self, master, title: str, entry_width: int, show: str = None):
        super().__init__(master)
        self.__title = Label(self, text=title)
        self.__title.pack()
        self.__entry = Entry(self, relief=SOLID, width=entry_width, show=show)
        self.__entry.pack()

    def get(self) -> str:
        return self.__entry.get()


