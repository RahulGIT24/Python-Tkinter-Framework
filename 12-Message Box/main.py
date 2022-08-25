from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x400")
root.title("Message Box")


def myFunc():
    print("I am a Function")


def help():
    print("I will help you")
    messagebox.showinfo("Help", "Rahul will help you with this gui") #! message.showinfo displays a dialog box, the syntax takes two arguments first is title second is message to be displayed


def rate():
    value = messagebox.askquestion(
        "Tell us about your experience", "You used this GUI was your experience good?")
    if value == 'yes':
        messagebox.showinfo("Thank You", "Thanks for a good rating")
    else:
        messagebox.showinfo("Thank You", "We will work on us")


def divya():
    ans = messagebox.askretrycancel(
        "Divya se dosti karlo", "Sorry nhi bnegi teri dost")
    if ans:
        messagebox.showinfo("Dosti ke naam do jaam",
                            "Kha na bhai nhi bnegi vo teri dost")
    else:
        messagebox.showinfo("Dosti ke naam do jaam",
                            "Waah Tu to sakht londa nikla....")

yourmenu = Menu(root)

m1 = Menu(yourmenu, tearoff=0)
m1.add_command(label="New File", command=myFunc)
m1.add_separator()
m1.add_command(label="Save", command=myFunc)
m1.add_command(label="Save as", command=myFunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="File", menu=m1)

m2 = Menu(yourmenu, tearoff=0)
m2.add_command(label="Copy", command=myFunc)
m2.add_separator()
m2.add_command(label="Cut", command=myFunc)
m2.add_command(label="Paste", command=myFunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(yourmenu, tearoff=0)
root.config(menu=yourmenu)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate", command=rate)
m3.add_command(label="Divya Ke dost banoge", command=divya)


yourmenu.add_cascade(label="Help", menu=m3)

root.mainloop()
