from tkinter import *
# * Creating 4 buttons and each button will print something in console

root = Tk()
root.geometry("770x400")
root.title("Buttons")

#! Creating Functions


def morningGreet():
    print("Good Morning, Rahul")


def afternoonGreet():
    print("Good Afternoonn, Rahul")


def eveningGreet():
    print("Good Evening, Rahul")


def nightGreet():
    print("Good Night, Rahul")


frame = Frame(root, bg="red", borderwidth=5, relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw", fill='x')
btn = Button(frame, bg="black", fg="red", text="Morning", command=morningGreet)
btn.pack(side=LEFT, padx=34)
btn1 = Button(frame, bg="black", fg="red",
              text="Afternoon", command=afternoonGreet)
btn1.pack(side=LEFT, padx=34)
btn2 = Button(frame, bg="black", fg="red",
              text="Evening", command=eveningGreet)
btn2.pack(side=LEFT, padx=34)
btn3 = Button(frame, bg="black", fg="red", text="Night", command=nightGreet)
btn3.pack(side=LEFT, padx=34)
btn4 = Button(frame, bg="black", fg="red", text="Exit", command=exit)
btn4.pack(side=LEFT, padx=34)

root.mainloop()
