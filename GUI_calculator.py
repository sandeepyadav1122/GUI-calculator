import tkinter as tk
import math

# Function to handle button clicks
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def add_to_display(value):
    entry.insert(tk.END, value)

def square_root():
    try:
        num = float(entry.get())
        result = math.sqrt(num)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Creating the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Styling for the buttons
button_style = {
    'font': ('Arial', 12),
    'width': 4,
    'height': 2,
    'bd': 1,
    'relief': 'ridge',
}

# Entry field to display input and output
entry = tk.Entry(root, width=30, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=5, pady=10)

# Buttons for calculator operations
buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', '√',
    '1', '2', '3', '-', '^',
    '0', '.', '=', '+', 'π'
]

# Function to handle button clicks
row = 1
col = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, command=evaluate, **button_style)
    elif button == 'C':
        btn = tk.Button(root, text=button, command=clear, **button_style)
    elif button == '√':
        btn = tk.Button(root, text=button, command=square_root, **button_style)
    else:
        btn = tk.Button(root, text=button, command=lambda x=button: add_to_display(x), **button_style)
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 4:
        col = 0
        row += 1

# Configure row and column weights to maintain 3*4 ratio
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()
