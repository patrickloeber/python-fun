import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cool Paint App")
        
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.button_clear = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.button_clear.pack()
        
        self.canvas.bind("<Button-1>", self.start_paint)
        self.canvas.bind("<B1-Motion>", self.paint)
        
        self.old_x = None
        self.old_y = None

    def start_paint(self, event):
        self.old_x = event.x
        self.old_y = event.y

    def paint(self, event):
        new_x = event.x
        new_y = event.y
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, new_x, new_y, fill="black", width=2)
        self.old_x = new_x
        self.old_y = new_y

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
