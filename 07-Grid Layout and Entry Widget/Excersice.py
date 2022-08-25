from tkinter import *
root = Tk()


def inforeturn():
    name = (f"The name of the person is {name_value.get()}")
    age = (f"The age of the person is {int(age_value.get())}")
    phno = (f"The Phone Number of the person is {int(number_value.get())}")
    address = (f"The address of the person is {address_value.get()}")
    with open("Registered Users.txt", 'w') as f:
        f.write(f'''{name}
{age}
{phno}
{address}''')
        print("Form submitted")


root.geometry("700x500")
root.minsize(700, 500)
root.maxsize(700, 500)

root.title("Dance Form")

label = Label(text="Fill Form to get admission in Dance Academy",
              bg='red', fg='black', pady=12, font="sans-serif 12 bold").grid()

name = Label(text="Enter your name")
age = Label(text="Enter your age")
number = Label(text="Enter your Phone Number")
address = Label(text="Enter your Address",)


name.grid(row=1)
age.grid(row=2)
number.grid(row=3)
address.grid(row=4)

name_value = StringVar()
age_value = StringVar()
number_value = StringVar()
address_value = StringVar()

name_entry = Entry(root, textvariable=name_value)
age_entry = Entry(root, textvariable=age_value)
number_entry = Entry(root, textvariable=number_value)
address_entry = Entry(root, textvariable=address_value)

name_entry.grid(row=1, column=1)
age_entry.grid(row=2, column=1)
number_entry.grid(row=3, column=1)
address_entry.grid(row=4, column=1)

Button(text="Submit", bg="black", fg="red",
       padx=12, pady=2, command=inforeturn).grid()

root.mainloop()
