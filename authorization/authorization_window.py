from tkinter import *


from templates import InputForm

#ПРИ НАЖАТИИ АВТОРИЗАЦИЯ
def authorization():
    window = Tk()
    window.title("Secret Notepad (АВТОРИЗАЦИЯ)")
    window.geometry('600x400')

    login_form = InputForm(window, 'ЛОГИН', 30) 
    login_form.pack(pady=15)

    password_form = InputForm(window, 'ПАРОЛЬ', 30, show='*')
    password_form.pack(pady=15)

    login_but = Button(window, width=15, text='ВОЙТИ', 
                  relief=SOLID, cursor='hand2', font=('Arial', 10), command=NONE)
    login_but.pack(pady=15)



    window.mainloop()

if __name__ == '__main__':
    authorization()

    


