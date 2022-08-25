from tkinter import *

root = Tk()


def getVal():
    print("Form Submitted")


root.geometry("300x300")
Label(text="Login Form", pady=5, bg="red", fg="black").grid()

name = Label(text="Username")
password = Label(text="Password")
name.grid(row=1)
password.grid(row=2)

nameValue = StringVar()
passValue = StringVar()

nameEntry = Entry(root,textvariable=nameValue)
passEntry = Entry(root,textvariable=passValue)

nameEntry.grid(row=1,column=3)
passEntry.grid(row=2,column=3)

Button(text="Submit",bg="yellow",fg="black",pady=4,padx=4,command=getVal).grid(row=3)

root.mainloop()
