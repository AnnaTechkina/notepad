from tkinter import *
from GUI.templates.base_window import *
from data_verification.chek import *

#ПРИ НАЖАТИИ АВТОРИЗАЦИЯ
class AuthorizationWindow(BaseInputWindow):
    def __init__(self):
        super().__init__("АВТОРИЗАЦИЯ", "600x800")

        self.__login_but = Button(self,
                                  width=15,
                                  text='ВОЙТИ',
                                  relief=SOLID,
                                  cursor='hand2',
                                  font=('Arial', 10),
                                  command=check_existence_login)
        self.__login_but.pack(pady=15)



if __name__ == '__main__':
    auth_win = AuthorizationWindow()
    auth_win.mainloop()

    


