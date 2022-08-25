from tkinter import *


class GUI(Tk): #* Created a GUI class inherited from tkinter
    def __init__(self): #* Now self is used instead of root
        super().__init__()
        self.geometry("650x500")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var,
                               relief=SUNKEN, anchor='w')
        self.statusbar.pack(side=BOTTOM, fill=X)

    def newFunc(self):
        print("Function is Running")
    
    def createButton(self,name):
        Button(self,text=name,command=self.newFunc).pack()
    
if __name__ == "__main__":
    window = GUI() #* Added all the things of GUI class in window variable
    window.status()
    window.createButton("Click Me")
    window.title("OOPS")
    window.mainloop()
