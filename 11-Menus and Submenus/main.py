from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Menus and Submenus")

def myFunc():
    print("I am a Function")

#! Use these to create a non drop down menu
# mymenu = Menu(root)
# mymenu.add_command(label="File",command=myFunc)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)

#! Use to create a drop down menu
yourmenu = Menu(root)

m1 = Menu(yourmenu,tearoff=0) #* This is the submenu

#* Creating various options in submenu
m1.add_command(label="New File",command=myFunc) #! myFunc will be fired when you click on new file sub menu
m1.add_separator()
m1.add_command(label="Save",command=myFunc)
m1.add_command(label="Save as",command=myFunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="File",menu=m1)

m2 = Menu(yourmenu,tearoff=0) #! tearoff=0 is given so that no line appears when you open menus to access submenus

m2.add_command(label="Copy",command=myFunc)
m2.add_separator()
m2.add_command(label="Cut",command=myFunc)
m2.add_command(label="Paste",command=myFunc)
root.config(menu=yourmenu)

#* add cascade is used when you have to add submenu title to menu
yourmenu.add_cascade(label="Edit",menu=m2)

root.mainloop()

