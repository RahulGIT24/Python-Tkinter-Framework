from tkinter import *
from PIL import Image, ImageTk


def new_line(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i % 100 == 0 and i != 0:
            final_text += "\n"
    return final_text


root = Tk()

root.title("Rahul's Newspaper")
width = "1000"
height = "1700"

root.geometry(f"{width}x{height}")

news = []
for i in range(0, 3):
    with open(f"{i+1}.txt", 'r') as f:
        read = f.read()
        news.append(new_line(read))

images = []
for i in range(0, 3):
    image = Image.open(f"{i+1}.png")
    image = image.resize((225, 225), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    images.append(photo)

f0 = Frame(root, height=70)
f0.pack()
headline = Label(f0, text="Welcome to Rahul's Newspaper",
                 font="sans-serif 22 bold")
headline.pack()
headline2 = Label(f0, text="Get latest news",
                  font="sans-serif 12 bold", pady=10)
headline2.pack()


f1 = Frame(root, height=200, width=900)
Label(f1, text=news[0], padx=22,
      font="sans-serif 11").pack(side="left")
Label(f1, image=images[0], anchor='e').pack()
f1.pack(anchor='w')

f2 = Frame(root, height=200, width=900, pady=22)
Label(f2, text=news[1], padx=22,
      font="sans-serif 11").pack(side="right")
Label(f2, image=images[1], anchor='w').pack(side="left")
f2.pack(anchor='e')

f3 = Frame(root, height=200, width=900, pady=22)
Label(f3, text=news[2], padx=22,
      font="sans-serif 11").pack(side="left")
Label(f3, image=images[2], anchor='e').pack()
f3.pack(anchor='w')


root.mainloop()
