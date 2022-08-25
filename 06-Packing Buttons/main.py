from tkinter import *

root = Tk()
root.geometry("600x700")


def hello():
    print("Hi Rahul")


frame = Frame(root, borderwidth=6, relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

# * Use to create a button
btn = Button(frame, fg="red", bg="black", text="Click Me!")
btn.pack(side=LEFT, padx=20)
btn2 = Button(frame, fg="red", bg="black", text="Click Me!",
              command=hello)  # * Through command we can use a function by clicking on the button it will be fired
btn2.pack(side=LEFT, padx=20)
btn3 = Button(frame, fg="red", bg="black", text="Click Me!")
btn3.pack(side=LEFT, padx=20)
btn4 = Button(frame, fg="red", bg="black", text="Click Me!")
btn4.pack(side=LEFT, padx=20)
btn5 = Button(frame, fg="red", bg="black", text="Click Me!")
btn5.pack(side=LEFT, padx=20)
btn6 = Button(frame, fg="red", bg="black", text="Click Me!")
btn6.pack(side=LEFT, padx=20)

root.mainloop()
