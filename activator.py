import tkinter as tk

def greet():
    name = entry.get()
    label_result.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("Simple App")

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Greet", command=greet)
btn.pack()

label_result = tk.Label(root)
label_result.pack()

root.mainloop()