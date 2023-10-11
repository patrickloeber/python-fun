import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file.set(file_path)

def browse_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        selected_directory.set(directory_path)

# Create the main window
root = tk.Tk()
root.title("Cool File Explorer")

# Create a label to display the selected file
selected_file = tk.StringVar()
file_label = tk.Label(root, textvariable=selected_file, font=('Helvetica', 12))
file_label.pack(pady=10)

# Create a button to browse for a file
file_button = tk.Button(root, text="Browse File", font=('Helvetica', 12), command=browse_file)
file_button.pack()

# Create a label to display the selected directory
selected_directory = tk.StringVar()
directory_label = tk.Label(root, textvariable=selected_directory, font=('Helvetica', 12))
directory_label.pack(pady=10)

# Create a button to browse for a directory
directory_button = tk.Button(root, text="Browse Directory", font=('Helvetica', 12), command=browse_directory)
directory_button.pack()

# Start the GUI main loop
root.mainloop()
