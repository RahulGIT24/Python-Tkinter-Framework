from tkinter import *

root = Tk()
root.geometry("700x400")
root.title("Scroll Bar")

#! For Connecting scroll Bar to a Widget
# * 1. widget (yscrollcommand= scrollbar.set)
# * 2. scroolbar.config(command = widget.yview)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

# listbox = Listbox(root, yscrollcommand=scroll.set)
# for i in range(344):
#     listbox.insert(END, f"Item {i}")

listbox = Text(root,yscrollcommand=scroll.set)

listbox.pack(fill="both", padx=22)
scroll.config(command=listbox.yview)
root.mainloop()
