from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Frames in Tkinter")

#! Syntax to create a frame 
#* Frames are just like the div of CSS, in it you can enter the data

fr = Frame(root, bg="red", borderwidth=5, relief=SUNKEN) #* Used to Create Frames
fr.pack(side=LEFT, fill='y', pady=45)

f2 = Frame(root, borderwidth=9, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill='x')


l = Label(fr, text="New Frame -  VS Code",
          font="sans-serif 14 bold", fg="green")
l.pack(pady=126)
l1 = Label(f2, text="Welcome to Sublime Text",
           font="sans-serif 14 bold", fg="green")
l1.pack()
root.mainloop()
