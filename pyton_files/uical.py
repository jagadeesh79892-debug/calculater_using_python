import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Display
display = tk.Entry(
    root,
    font=("Arial", 22),
    bd=0,
    bg="#252526",
    fg="white",
    justify="right"
)
display.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# Button click function
def click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))

# Clear display
def clear():
    display.delete(0, tk.END)

# Calculate result
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Button frame
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

# Button style
btn_font = ("Arial", 14)
btn_bg = "#333333"
btn_fg = "white"
op_bg = "#ff9500"

# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
]

# Create number buttons
for row in buttons:
    row_frame = tk.Frame(frame, bg="#1e1e1e")
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "C":
            action = clear
        else:
            action = lambda x=btn: click(x)

        color = op_bg if btn in "+-*/" else btn_bg

        tk.Button(
            row_frame,
            text=btn,
            font=btn_font,
            bg=color,
            fg=btn_fg,
            bd=0,
            command=action,
            height=2,
            width=5
        ).pack(side="left", expand=True, fill="both", padx=2, pady=2)

# Equal button
equal_frame = tk.Frame(frame, bg="#1e1e1e")
equal_frame.pack(expand=True, fill="both")

tk.Button(
    equal_frame,
    text="=",
    font=("Arial", 16),
    bg="#4CAF50",
    fg="white",
    bd=0,
    command=calculate,
    height=2
).pack(fill="both", expand=True, padx=2, pady=2)

# Run program
root.mainloop()