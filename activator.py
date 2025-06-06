import tkinter as tk
from tkinter import filedialog


def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
    )
    file_var.set(file_path) 
    print(file_var.get())

root = tk.Tk()
root.title("Aerosense Activator")
root.geometry("800x600")

file_var = tk.StringVar()

btn = tk.Button(root, text="Select File", command=select_file)
btn.pack()

label_file = tk.Label(root, textvariable=file_var)
label_file.pack()

root.mainloop()