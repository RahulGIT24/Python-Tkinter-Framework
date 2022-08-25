from tkinter import *
from PIL import Image, ImageTk #* This module is used to add .jpg images in a GUI

new_root = Tk()

new_root.geometry("444x444")

#! Adding Image
# photo = PhotoImage(file="1.png") #* Loading Png images in photo variable

#! For jpg images
image = Image.open("2.jpg")  # * Opening an Image
photo = ImageTk.PhotoImage(image) # * Loading the opened image in a variable using image.tk

chat_label = Label(image=photo)
chat_label.pack()

new_root.mainloop()
