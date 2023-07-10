from tkinter import *
from GUI.templates import InputForm, BaseInputWindow


class RegistrationWindow(BaseInputWindow):
    def __init__(self):
        super().__init__("РЕГИСТРАЦИЯ", "600x800")

        self.__password_form2 = InputForm(self, 'ПОВТОРИТЕ ПАРОЛЬ', 30, show='*')
        self.__password_form2.pack(pady=12)

        self.__login_but = Button(self,
                                  width=15,
                                  text='СОХРАНИТЬ',
                                  relief=SOLID,
                                  cursor='hand2',
                                  font=('Arial', 10),
                                  command=None)
        self.__login_but.pack(pady=15)

    def get(self):
        result = self.get()
        result.append(self.__password_form2.get())
        return result


if __name__ == '__main__':
    reg_win = RegistrationWindow()
    reg_win.mainloop()
