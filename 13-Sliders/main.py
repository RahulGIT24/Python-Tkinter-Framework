from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("700x650")
root.title("Sliders")


def getDollars():
    messagebox.showinfo(
        "Dollar Info", f"We have credited {mySlider2.get()} dollars to your bank account")

#! Used to create a vertical slider
# mySlider = Scale(root, from_=0, to=100)
# mySlider.pack()


Label(root, text="How many dollars do you want?").pack()

#! Used to create a horizontal slider
mySlider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
mySlider2.set(34)  # * Used to set default value
mySlider2.pack()

Button(root, text="Get Dollars", command=getDollars).pack()

root.mainloop()
