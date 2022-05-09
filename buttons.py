from tkinter import *

root = Tk()


# Functions ---------------------------------------
# -------------------------------------------------
def my_click():
    my_label = Label(root, text="Look, I clicked a button!")
    my_label.pack()


# Widgets -----------------------------------------
# -------------------------------------------------
# Creates a button widget
# adding state=DISABLED to button parameters will disable the button, but keep visibility
# padx and pady will add padding to either the x or y dimensions of a widget
# command=function_name can be used to link a button to a function. In this context
# it's important to exclude the parenthesis that would normally come with a function
my_button = Button(root, text="Click Me!", padx=50, pady=50, command=my_click)
# So far, we've set all the widget options at the creation of the widget. But we can
# also set them after the fact with the config() method
# inside the config method, we set the foreground-text(fg) to "blue" and the
# background(bg) to "red"
my_button.config(fg="blue", bg="#ccff00")



# Placement of widgets ----------------------------
# -------------------------------------------------
my_button.pack()

root.mainloop()
