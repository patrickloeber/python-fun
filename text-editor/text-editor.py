import tkinter as tk
from tkinter import filedialog, scrolledtext

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
            root.title(f"Cool Text Editor - {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
            root.title(f"Cool Text Editor - {file_path}")

# Create the main window
root = tk.Tk()
root.title("Cool Text Editor")

# Create a scrolled text widget
text = scrolledtext.ScrolledText(root, font=('Helvetica', 14))
text.pack(expand=True, fill='both')

# Create the menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Start the GUI main loop
root.mainloop()
