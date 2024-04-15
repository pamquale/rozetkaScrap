import tkinter as tk
import json


with open('phones.json', 'r', encoding='utf-8') as f:
    phone_data = json.load(f)


root = tk.Tk()
root.title("Phone Data")


listbox = tk.Listbox(root, width=100)
listbox.pack()


for phone in phone_data:
    listbox.insert(tk.END, f"Name: {phone['Name']}, Price: {phone['Price']}")


root.mainloop()
