import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

# Create the main window
root = tk.Tk()
root.title("Cool To-Do List")

# Entry widget for adding tasks
entry = tk.Entry(root, font=('Helvetica', 18))
entry.grid(row=0, column=0, columnspan=2)

# Button to add tasks
add_button = tk.Button(root, text="Add", font=('Helvetica', 14), command=add_task)
add_button.grid(row=0, column=2)

# Button to remove tasks
remove_button = tk.Button(root, text="Remove", font=('Helvetica', 14), command=remove_task)
remove_button.grid(row=0, column=3)

# Listbox to display tasks
listbox = tk.Listbox(root, font=('Helvetica', 18), selectmode=tk.SINGLE, selectbackground="#a5a5a5")
listbox.grid(row=1, column=0, columnspan=4)

# Start the GUI main loop
root.mainloop()
