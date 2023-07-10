from tkinter import Tk


class BaseWindow(Tk):
    def __init__(self, title: str, geometry: str):
        super().__init__()
        self.title(title)
        self.geometry(geometry)