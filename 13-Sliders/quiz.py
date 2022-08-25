from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("750x400")
root.title("Slider Quiz")


def userExp():
    if expSlider.get() <= 4:
        messagebox.showinfo(
            "Thanks", "We will try to improve ouself. Btw Thanks for rating")
        print(f"Your consumer has given us {expSlider.get()} rating")
    else:
        messagebox.showinfo("Thanks", "Thanks for rating us...")
        print(f"Your consumer has given us {expSlider.get()} rating")
    with open("Consumer rating.txt", 'w') as f:
        f.write(f"The last consumer has given you {expSlider.get()} rating")


Label(root, text="Enter your Experience!!", font="sans-serif 15 bold").pack()

expSlider = Scale(root, from_=0, to=10, orient=HORIZONTAL)
expSlider.pack()
Button(root, text="Submit", pady=6, padx=6, bg="red",
       fg="black", font="sans-serif 12 bold", command=userExp).pack()

root.mainloop()
