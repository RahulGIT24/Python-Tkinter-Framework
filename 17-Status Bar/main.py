from tkinter import *
import time

root = Tk()
root.geometry("650x400")
root.title("Status Bar")


def upload():
    statusvar.set("Busy....")
    sbar.update()
    time.sleep(2)
    statusvar.set("Ready Now")


statusvar = StringVar()
statusvar.set("Ready")

sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor='w')
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", padx=5, pady=5, command=upload).pack()

root.mainloop()
