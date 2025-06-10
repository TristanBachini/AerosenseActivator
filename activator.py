import tkinter as tk
from tkinter import filedialog, ttk


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
btn.grid(row=0, column=0, padx=10, pady=10)

label_file = tk.Label(root, textvariable=file_var)
label_file.grid(row=0, column=1, padx=10, pady=10)


#text entries
label_recepient = tk.Label(root, text="Recepient")
label_recepient.grid(row=1, column=0, padx=10, pady=10)

label_company = tk.Label(root, text="Company")
label_company.grid(row=2, column=0, padx=10, pady=10)

label_track = tk.Label(root, text="Tracking Number")
label_track.grid(row=3, column=0, padx=10, pady=10)

label_caredaily = tk.Label(root, text="Where to activate?")
label_caredaily.grid(row=4, column=0, padx=10, pady=10)

# Input field
entry = tk.Entry(root, width=30)
entry.grid(row=1, column=1, padx=10, pady=10)

entry = tk.Entry(root, width=30)
entry.grid(row=2, column=1, padx=10, pady=10)

entry = tk.Entry(root, width=30)
entry.grid(row=3, column=1, padx=10, pady=10)

entry = ttk.Combobox(root, textvariable=tk.StringVar(), values=["Caredaily Prod", "Caredaily Sandbox","Axend",""], state="readonly")
entry.grid(row=4, column=1, padx=10, pady=10)
root.mainloop()