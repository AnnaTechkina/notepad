from tkinter import *
from authorization import authorization
from registration import registration

#главное окно 
window = Tk()
window.title("SECRET Notepad")
window.geometry('300x200')


auth_btn = Button(window, width=15, text='АВТОРИЗАЦИЯ', 
                  relief=SOLID, cursor='hand2', font=('Arial', 15), command=authorization)
auth_btn.pack(pady=15)

reg_btn = Button(window, width=15, text='РЕГИСТРАЦИЯ',
                 relief=SOLID, cursor='hand2', font=('Arial', 15), command=registration)
reg_btn.pack(pady=15)


window.mainloop()




