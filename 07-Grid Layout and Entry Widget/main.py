from tkinter import *
def getVals():
    print(f"The name of the user is {uservalue.get()}")
    print(f"Password of the user is {passvalue.get()}")
    
root = Tk()

root.geometry("500x500")

# * Grid, it is like an excel sheet where there is rows and columns
l1 = Label(text="User Name")
l2 = Label(text="Password")
l1.grid()
l2.grid(row=1)  # * Packing using Grid

#! Variable Classes in tkinter
#* BooleanVar, StringVar, DoubleVar, IntVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getVals).grid()

root.mainloop()
