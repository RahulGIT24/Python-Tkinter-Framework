from tkinter import *

root = Tk()
root.geometry("655x444")
root.title("More On tkinter")

#! Change icon on GUI
root.wm_iconbitmap("vol.png")

#! Configure Function
root.configure(bg="gray")  # * Using Configure you can make changes to your GUI

#! These function will get the height and width of your screen
width = root.winfo_screenmmwidth()
height = root.winfo_screenheight()
print(f"{width}X{height}")

# * Destroy function used to close a window
Button(text="Close", command=root.destroy).pack()


root.mainloop()
