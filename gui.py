import tkinter as tk
import json

with open('phones.json', 'r', encoding='utf-8') as f:
    phone_data = json.load(f)

root = tk.Tk()
root.title("Phone Data")

listbox = tk.Listbox(root, width=100)
listbox.pack()

# Create Entry fields for Name, Price, Storage and Color
name_var = tk.StringVar()
price_var = tk.StringVar()
storage_var = tk.StringVar()
color_var = tk.StringVar()

name_entry = tk.Entry(root, textvariable=name_var, width=50)
price_entry = tk.Entry(root, textvariable=price_var, width=50)
storage_entry = tk.Entry(root, textvariable=storage_var, width=50)
color_entry = tk.Entry(root, textvariable=color_var, width=50)

name_entry.pack()
price_entry.pack()
storage_entry.pack()
color_entry.pack()


def update_item():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        new_name = name_var.get()
        new_price = price_var.get()
        new_storage = storage_var.get()
        new_color = color_var.get()
        phone_data[index]['Name'] = new_name
        phone_data[index]['Price'] = new_price
        phone_data[index]['Storage'] = new_storage
        phone_data[index]['Color'] = new_color
        listbox.delete(index)
        listbox.insert(index, f"Name: {new_name}, Price: {new_price}, Storage: {new_storage}, Color: {new_color}")


update_button = tk.Button(root, text="Update Item", command=update_item)
update_button.pack()

for phone in phone_data:
    listbox.insert(tk.END, f"Name: {phone['Name']}, Price: {phone['Price']}, Storage: {phone['Storage']}, Color: {phone['Color']}")

root.mainloop()