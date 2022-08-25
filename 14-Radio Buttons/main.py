from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x400")
root.title("Radio Buttons")

# var = IntVar()  # * Initialized a variable
var = StringVar()

#! Don't Forget to set varible's value
var.set('1')  # * Setting value in a variable

Label(root, text="What do like to want sir?",
      justify=RIGHT, padx=14, font="Lucida 13 bold").pack()


def order():
    messagebox.showinfo(
        "Order Received", f"We have received your order for {var.get()}. Thanks for ordering")

#! Creating a radio button


radio = Radiobutton(root, text="Dosa", padx=18,
                    variable=var, value="Dosa").pack(anchor='w')
radio = Radiobutton(root, text="Tikki", padx=18,
                    variable=var, value="Tikki").pack(anchor='w')
radio = Radiobutton(root, text="Samosa", padx=18,
                    variable=var, value="Samosa").pack(anchor='w')
radio = Radiobutton(root, text="Burger", padx=18,
                    variable=var, value="Burger").pack(anchor='w')

Button(text="Order Now", command=order).pack()

root.mainloop()
