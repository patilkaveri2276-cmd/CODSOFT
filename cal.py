import tkinter as tk

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry display
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Function to add value to screen
def click(value):
    entry.insert(tk.END, value)

# Clear screen
def clear():
    entry.delete(0, tk.END)

# Calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('C','0','=','+')
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    
    for btn in row:
        button = tk.Button(frame, text=btn, font=("Arial", 18))
        button.pack(side="left", expand=True, fill="both")

        if btn == "=":
            button.config(command=calculate, bg="lightgreen")
        elif btn == "C":
            button.config(command=clear, bg="lightcoral")
        else:
            button.config(command=lambda b=btn: click(b))

root.mainloop()
