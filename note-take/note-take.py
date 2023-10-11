import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog

def save_note():
    note = text_widget.get("1.0", "end-1c")  # Get text from the text widget
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if file_path:
        with open(file_path, 'w') as file:
            file.write(note)

def open_note():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    if file_path:
        with open(file_path, 'r') as file:
            note = file.read()
            text_widget.delete("1.0", "end")  # Clear existing text
            text_widget.insert("1.0", note)  # Insert the loaded note

# Create the main window
root = tk.Tk()
root.title("Cool Note Taker")

# Create a scrolled text widget
text_widget = scrolledtext.ScrolledText(root, font=('Helvetica', 14))
text_widget.pack(expand=True, fill='both')

# Create "Save" and "Open" buttons
save_button = tk.Button(root, text="Save Note", font=('Helvetica', 12), command=save_note)
save_button.pack(side="left", padx=10, pady=10)

open_button = tk.Button(root, text="Open Note", font=('Helvetica', 12), command=open_note)
open_button.pack(side="right", padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
