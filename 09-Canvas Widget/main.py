from tkinter import *

root = Tk()

root.title("Canvas Widget")
canvas_width = 650
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")

#! Canvas Widget

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

#! The line goes from the point x1,y1,x2,y2
can_widget.create_line(0, 0, 800, 400, fill='red')  # * Used to create a line
can_widget.create_line(0, 400, 800, 0, fill='red')

#! To create a rectangle dpecify parameters in this order - coors of top left and coors of bottom right
# * Used to create a rectangle
can_widget.create_rectangle(3, 5, 700, 300, fill='blue')

can_widget.create_text(200, 200, text="Python")  # * Used to create text

can_widget.create_oval(200, 200, 400, 400)  # * To create an oval

can_widget.create_arc(200, 400, 350, 190)


root.mainloop()
