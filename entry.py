from tkinter import *

root = Tk()


# Functions ---------------------------------------
# -------------------------------------------------
def my_click():
    hello = "Hello " + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()


# Widgets -----------------------------------------
# -------------------------------------------------
my_button = Button(root, text="Enter your name", command=my_click)

# Adds an entry widget
e = Entry(root, width=50)
# the get() method will "get" the text within the entry field
# focus_set() method puts the focus immediately on this widget
e.focus_set()
e.insert(0, "Enter Your Name: ")




# Placement of widgets ----------------------------
# -------------------------------------------------
my_button.pack()
e.pack()

root.mainloop()
