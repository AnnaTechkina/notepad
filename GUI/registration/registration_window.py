from tkinter import *
from GUI.templates import InputForm, BaseWindow


class RegistrationWindow(BaseWindow):
    def __init__(self, title: str, geometry: str):
        super().__init__("РЕГИСТРАЦИЯ", "600x800")
        login_form = InputForm(self, 'ЛОГИН', 30)
        login_form.pack(pady=15)

        password_form = InputForm(self, 'ПАРОЛЬ', 30, show='*')
        password_form.pack(pady=15)

        password_form2 = InputForm(self, 'ПОВТОРИТЕ ПАРОЛЬ', 30, show='*')
        password_form2.pack(pady=12)

        login_but = Button(self,
                           width=15,
                           text='СОХРАНИТЬ',
                           relief=SOLID,
                           cursor='hand2',
                           font=('Arial', 10),
                           command=None)
        login_but.pack(pady=15)


if __name__ == '__main__':
    reg_win = RegistrationWindow()
    reg_win.mainloop()
