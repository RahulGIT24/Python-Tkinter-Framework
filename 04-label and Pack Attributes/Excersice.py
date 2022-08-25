from tkinter import *

root = Tk()

root.geometry("500x400")

root.title("Tkinter Challenge 1")
text_label = Label(text="Ready",bg="red",foreground="white", font="sans-serif 34 bold")
text_label.pack(side=BOTTOM, fill=X)

root.mainloop()