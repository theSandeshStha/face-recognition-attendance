from tkinter import *
from tkinter import messagebox
import os
from main import Face_Recognition_System

root = Tk()
root.title("Login")
root.geometry('925x500+300+200')
root.configure(bg = '#fff')
root.resizable(False, False)

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text = 'Sign in', fg="#57a1f8", bg='white', font=('Microsoft YaHei UI Light', 23))
heading.place(x=100, y=5)


# Username field
def on_enter(e):
    user.delete(0, 'end')


def on_exit(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_exit)

#black line
Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


# Password field
def on_in(e):
    pw.delete(0, 'end')


def on_out(e):
    name = pw.get()
    if name == '':
        pw.insert(0, 'Password')

pw = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
pw.place(x=30, y=150)
pw.insert(0, "Password")
pw.bind('<FocusIn>', on_in)
pw.bind('<FocusOut>', on_out)

#black line
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

#Sign in button

def signin():
    username = user.get()
    password = pw.get()

    if username == 'admin' and password == '1234':
        new_window = Toplevel(root)
        app = Face_Recognition_System(new_window)
    else:
        messagebox.showerror("Invalid", "Invalid username or password!")

Button(frame, width=29, pady=7, text="Sign in", bg="#57a1f8", fg="black", border=0, command=signin).place(x=35, y=204)


root.mainloop()