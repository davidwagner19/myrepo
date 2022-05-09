from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("360x400")

# --------------- to do ---------------------------
# -------------------------------------------------
# TODO - add buttons for subtraction, multiplication, division, decimal, neg/pos, and del
# buttons have been added but still need to be properly fitted.
# TODO - decimal function
# TODO - neg/pos function
# TODO - subtraction function
# TODO - multiplication function
# TODO - division function
# TODO - improve visual design? maybe...
# FIXME - after expression is evaluated, numbers can still be added to the entry widget
# FIXME - multiplication and division of zero may be an issue


# Functions ---------------------------------------
# -------------------------------------------------
def button_click(number):
    # We only want to use the buttons for input into the entry, so the entry widget state will
    # be disabled by default and only turned on when a button is used.
    e.config(state="normal")
    # Ensures no leading zeros are left
    if e.get() == "0":
        e.delete(0, END)
    e.insert(END, number)
    e.config(state="disabled")


def button_add():
    """Adds the number in the entry field and '+' operator to the expression. Resets entry field."""
    global nums
    global operators
    # the current number is stored into nums
    nums.append(e.get())
    # the addition operator is stored into operators
    operators.append("+")
    e.config(state="normal")
    e.delete(0, END)
    e.insert(0, "0")
    e.config(state="disabled")
    print(nums)
    print(operators)


def button_equal():
    """Evaluates the expression stored in the calculator and displays it."""
    global nums
    global operators
    # the current number is stored into nums
    nums.append(e.get())
    # the equal operator is stored into operators
    operators.append("=")
    # a blank expression is started and then populated by the numbers and operators
    expression = ""
    for i in range(len(nums)):
        expression += nums[i]
        expression += operators[i]
    expression = expression.strip("=")
    solution = eval(expression)
    print(solution)
    e.config(state="normal")
    e.delete(0, END)
    e.insert(0, solution)
    e.config(state="disabled")
    nums.clear()
    operators.clear()
    print(nums)
    print(operators)


def button_clear():
    """Resets the Calculator."""
    global nums
    global operators
    e.config(state="normal")
    e.delete(0, END)
    e.insert(0, "0")
    e.config(state="disabled")
    nums.clear()
    operators.clear()
    print(nums)
    print(operators)


# Calculate Expression ----------------------------
# -------------------------------------------------
# All the numbers used in the expression
nums = []
# All the operators used in the expression
operators = []

# Widgets -----------------------------------------
# -------------------------------------------------
# define buttons
# Row 1 (top)
button_clear = Button(root, text="Clear", padx=70, pady=20, command=button_clear)
button_del = Button(root, text="del", padx=36, pady=20, command=button_add)
button_divide = Button(root, text="/", padx=36, pady=20, command=button_add)
# Row 2
button_7 = Button(root, text="7", padx=35, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=35, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=35, pady=20, command=lambda: button_click(9))
button_multiply = Button(root, text="x", padx=35, pady=20, command=button_add)
# Row 3
button_4 = Button(root, text="4", padx=35, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=35, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=35, pady=20, command=lambda: button_click(6))
button_subtract = Button(root, text="-", padx=35, pady=20, command=button_add)
# Row 4
button_1 = Button(root, text="1", padx=35, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=35, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=35, pady=20, command=lambda: button_click(3))
button_add = Button(root, text="+", padx=35, pady=20, command=button_add)
# Row 5 (Bottom)
button_0 = Button(root, text="0", padx=35, pady=20, command=lambda: button_click(0))
button_decimal = Button(root, text=".", padx=35, pady=20, command=button_add)
button_pos_neg = Button(root, text="+/-", padx=30, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=35, pady=20, command=button_equal)


# Adds an entry widget
e = Entry(root, width=50, borderwidth=5, justify="right")
# insert() method places text inside an entry widget
# Sets the entry field to "0" by default
e.insert(0, "0")
# disables typing for the user to eliminate unusable characters
e.config(state="disabled")

# Placement of widgets ----------------------------
# -------------------------------------------------
# Top (Entry Field)
e.grid(row=0, column=0, columnspan=4, padx=0, pady=10)
# Row 1
button_clear.grid(row=1, column=0, columnspan=2)
button_del.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

# Row 2
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

# Row 3
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

# Row 4
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

# Row 5
button_0.grid(row=5, column=0)
button_decimal.grid(row=5, column=1)
button_pos_neg.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

# window loop
root.mainloop()
