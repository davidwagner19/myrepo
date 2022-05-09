from tkinter import *
# ttk is a tkinter module that allows the use of themed widgets
# introduced from tk 8.5 onward

# Creating a root window that everything will be placed into
root = Tk()

# Creating a label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is David Wagner")

# You can use .pack() to shove it onto the screen/window
# myLabel1.pack()

# Or you can use the grid method to create, well, a grid
myLabel1.grid(row=0, column=0)
# One thing to remember is that columns and rows will only be as large as the
# items that populate them. If they're empty, they'll barely be visible at all
myLabel2.grid(row=1, column=5)

# The mainloop is necessary to keep the window up
# essentially the window itself is the mainloop, updating until closed by the user
root.mainloop()
