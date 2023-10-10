import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

# Create the main window
root = tk.Tk()
root.title("Cool Image Viewer")

# Create a label to display the image
label = tk.Label(root)
label.pack()

# Create a button to open an image
open_button = tk.Button(root, text="Open Image", font=('Helvetica', 14), command=open_image)
open_button.pack()

# Start the GUI main loop
root.mainloop()
