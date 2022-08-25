from tkinter import *
root = Tk()

root.geometry("900x233")

root.title("Rahul's GUI")  # * Used to add title

#! Important Label Options

# * text - Used to add text
# * bg - background
# * fg - foreground
# * font - sets the font
#! 1. font=("sans-serif", 12, "bold")
#! 2. font="sans-serif 14 bold"
# * padx - padding in x
# * pady - padding in y
# * relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE



text_label = Label(text='''An article is any member of a class of dedicated words that are used with \nnoun phrases to mark the identifiability of the referents of the noun phrases. The category of \narticles constitutes a part of speech. In English, both "the" and are articles, which combine \nwith nouns to form noun phrases.''',
                   bg="green", fg="white", padx=23, pady=43, font="sans-serif 14 bold", borderwidth=3, relief=GROOVE)



#! Important Pack Options
# * anchor = "nw" (north west)
# * side = top, bottom, left, right
# fill
# padx
# pady

# text_label.pack(side=BOTTOM, anchor="sw", fill=X)
text_label.pack(side=LEFT, fill=Y, padx=45, pady=67)

root.mainloop()
