from tkinter import *


def harry(event):
    print(f"You clicked on harry {event.x} {event.y}")


root = Tk()
root.geometry("650x350")
root.title("Event handling")

widget = Button(root, text="Click Me!")
widget.pack()

# ! bind function is used to add event in a button

# * Here you have to give two arguments the first one is like when you click or double click and second one is the function you want to run
widget.bind("<Button-1>", harry)


# * exit or quit is a predefined function so you can use them without defining them it will close the program
widget.bind("<Double-1>", exit)

root.mainloop()
