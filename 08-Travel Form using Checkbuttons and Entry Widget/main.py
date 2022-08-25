from tkinter import *
root = Tk()

root.geometry("700x500")

# * This function will store the entered data in Records.txt file


def getVals():
    info = (f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodservicevalue.get()}\n")
    with open("Records.txt", "a") as f:
        f.write(info)


Label(text="Welcome to Rahul Travels",
      font="sans-serif 12 bold", pady=15, padx=12).grid(row=0, column=3)
name = Label(root, text="Name")
phone = Label(root, text="Phone Number")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact Number")
paymentmode = Label(root, text="Payment Method")


name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)


namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

# * Entry is used to when we want to allow user to enter some data just like a form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymententry = Entry(root, textvariable=paymentvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)


# *Checkbutton is used to create a checkbox

foodservice = Checkbutton(
    text="Want to prebook your meals", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

#! When we select a checkbox i's return value is 1 and by default 0

Button(text="Submit to Rahul Travels", bg="red", fg="white", pady=4, padx=2,
       borderwidth=3, relief=SUNKEN, command=getVals).grid(row=7, column=3)

root.mainloop()
