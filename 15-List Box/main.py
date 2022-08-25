from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("List Box")


def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i += 1


i = 0

# * Used to add a list box
lbx = Listbox(root)
lbx.insert(END, "First Item of a list box")

lbx.pack()

Button(root, text="Add Item", command=add).pack()

root.mainloop()
