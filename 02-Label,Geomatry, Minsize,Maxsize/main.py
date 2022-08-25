from tkinter import *

new_root = Tk()

#! WidthxHeight
new_root.geometry("520x500")

#! Width,Height
new_root.minsize(500,500) #* Set minimum Size of window
new_root.maxsize(700,700) #* Set maximum Size of window

#! Creating Label
rahul = Label(text="This is tkinter gui")
rahul.pack() #* Don't forgot to pack label

new_root.mainloop()