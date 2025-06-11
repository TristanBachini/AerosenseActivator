import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import requests
import json
import pandas as pd


def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
    )
    file_var.set(file_path) 
    print(file_var.get())

def activate():
    url = "http://34.199.190.12:8080/inner/manager/application/assign-radar"

    radars = pd.read_excel(file_var.get())
    print(type(radars))

    payload = json.dumps({
   "appId": "XgusEhYd",
   "radarIds": []
    })

    headers = {
   'Content-Type': 'application/json'
    }


    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    messagebox.showinfo("Yes!","Yahoo!")

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
entry_recepient = tk.Entry(root, width=30)
entry_recepient.grid(row=1, column=1, padx=10, pady=10)

entry_company = tk.Entry(root, width=30)
entry_company.grid(row=2, column=1, padx=10, pady=10)

entry_track = tk.Entry(root, width=30)
entry_track.grid(row=3, column=1, padx=10, pady=10)

entry_caredaily = ttk.Combobox(root, textvariable=tk.StringVar(), values=["Caredaily Prod", "Caredaily Sandbox","Axend","None Of The Above"], state="readonly")
entry_caredaily.grid(row=4, column=1, padx=10, pady=10)

submit_btn = tk.Button(root, text="Submit", command=activate)
submit_btn.grid(row=5, column=0, padx=10, pady=10)


root.mainloop()

