import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Function to load JSON data
def load_json():
    with open('iphone_models.json', 'r') as f:
        return json.load(f)

# Function to save JSON data
def save_json(data):
    with open('iphone_models.json', 'w') as f:
        json.dump(data, f, indent=4)

# Function to update the treeview with JSON data
def update_treeview():
    for item in tree.get_children():
        tree.delete(item)
    for i, model in enumerate(data):
        tree.insert("", "end", iid=i, values=(
            model["Name"], model["Part Number"], model["Colors"],
            model["RAM"], model["Price"], model["Storage"]
        ))

# Function to save edits
def save_edits():
    selected_item = tree.selection()[0]
    for i, field in enumerate(fields):
        data[int(selected_item)][field] = entries[i].get()
    save_json(data)
    update_treeview()
    messagebox.showinfo("Info", "Changes saved successfully")

# Function to populate entry fields when an item is selected
def on_item_selected(event):
    selected_item = tree.selection()[0]
    model = data[int(selected_item)]
    for i, field in enumerate(fields):
        entries[i].delete(0, END)
        entries[i].insert(0, model[field])

# Load JSON data
data = load_json()

# Create main window
root = Tk()
root.title("iPhone Models Editor")
root.geometry("1000x400")

# Create a treeview widget
columns = ["Name", "Part Number", "Colors", "RAM", "Price", "Storage"]
tree = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill=BOTH, expand=True)

# Add scrollbar
scrollbar = Scrollbar(tree, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)

# Update treeview with data
update_treeview()

# Bind the item selection event
tree.bind('<<TreeviewSelect>>', on_item_selected)

# Create edit section
edit_frame = Frame(root)
edit_frame.pack(pady=10)

fields = ["Name", "Part Number", "Colors", "RAM", "Price", "Storage"]
entries = []

for field in fields:
    frame = Frame(edit_frame)
    frame.pack(fill=X, padx=5, pady=5)
    label = Label(frame, text=field, width=15)
    label.pack(side=LEFT)
    entry = Entry(frame)
    entry.pack(side=RIGHT, fill=X, expand=True)
    entries.append(entry)

# Create save button
save_button = Button(root, text="Save Changes", command=save_edits)
save_button.pack(pady=10)

# Main loop
root.mainloop()
