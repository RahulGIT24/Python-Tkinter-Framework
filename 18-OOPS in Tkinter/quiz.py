from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('650x400')

    #! Functions Here
    def form(self):
        self.heading = Label(self, text="Enter your details here",
                             font="Lucida 13 bold").grid(column=6)
        self.name = Label(self, text="Name", pady=12).grid(row=1, column=0)
        self.password = Label(self, text="Password",
                              pady=12).grid(row=2, column=0)

        self.namevalue = StringVar()
        self.passvalue = StringVar()

        self.nameentry = Entry(
            self, textvariable=self.namevalue).grid(row=1, column=3)
        self.passeentry = Entry(
            self, textvariable=self.passvalue).grid(row=2, column=3)

    def getVals(self):
        print(f"Name of the user is {self.namevalue.get()}")
        print(
            f"Password of {self.namevalue.get()} is {self.passvalue.get()}")

    def createButton(self, inputText):
        Button(self, text=inputText, command=self.getVals).grid(row=3)


if __name__ == '__main__':
    win = GUI()
    win.title("OOPS in tkinter quiz")
    win.form()
    win.createButton("SUBMIT")
    win.mainloop()
