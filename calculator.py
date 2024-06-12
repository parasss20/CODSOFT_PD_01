import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")

# Create an Entry widget for displaying the result
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Function to update the entry widget when buttons are pressed
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to clear the entry widget
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Define button labels and their positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons in the grid
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=10, height=3, command=button_equal).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, width=10, height=3, command=button_clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=10, height=3, command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Run the main loop
root.mainloop()
