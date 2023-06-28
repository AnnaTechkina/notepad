from tkinter import *
from templates.form import InputForm


def registration():
    window = Tk()
    window.title("Secret Notepad (РЕГИСТРАЦИЯ)")
    window.geometry('600x400')

    login_form = InputForm(window, 'ЛОГИН', 30)
    login_form.pack(pady=15)

    password_form = InputForm(window, 'ПАРОЛЬ', 30, show='*')
    password_form.pack(pady=15)

    password_form2 = InputForm(window, 'ПОВТОРИТЕ ПАРОЛЬ', 30, show='*')
    password_form2.pack(pady=12)

    login_but = Button(window, width=15, text='СОХРАНИТЬ',
                       relief=SOLID, cursor='hand2', font=('Arial', 10), command=None)
    login_but.pack(pady=15)

    window.mainloop()


if __name__ == '__main__':
    registration()
