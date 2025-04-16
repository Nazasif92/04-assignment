import tkinter as tk

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")
        
        # Canvas size and grid settings
        self.canvas_width = 400
        self.canvas_height = 400
        self.cell_size = 20
        
        # Create canvas
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Draw grid of blue cells
        self.cells = []
        for i in range(0, self.canvas_width, self.cell_size):
            row = []
            for j in range(0, self.canvas_height, self.cell_size):
                rect = self.canvas.create_rectangle(i, j, i + self.cell_size, j + self.cell_size, fill="blue")
                row.append(rect)
            self.cells.append(row)

        # Create an eraser (initially at the top left corner)
        self.eraser = self.canvas.create_rectangle(0, 0, self.cell_size, self.cell_size, fill="white", outline="black")
        
        # Store the position of the eraser
        self.eraser_pos = [0, 0]

        # Bind mouse events for dragging the eraser
        self.canvas.bind("<B1-Motion>", self.on_drag)

    def on_drag(self, event):
        # Calculate the new position of the eraser based on mouse position
        x = (event.x // self.cell_size) * self.cell_size
        y = (event.y // self.cell_size) * self.cell_size
        
        # Move the eraser rectangle
        self.canvas.coords(self.eraser, x, y, x + self.cell_size, y + self.cell_size)
        
        # Update the eraser's position
        self.eraser_pos = [x, y]
        
        # Erase cells by changing color to white
        self.erase_cells(x, y)

    def erase_cells(self, x, y):
        # Determine the bounds of the eraser
        start_x = x // self.cell_size
        start_y = y // self.cell_size
        end_x = (x + self.cell_size - 1) // self.cell_size
        end_y = (y + self.cell_size - 1) // self.cell_size
        
        # Set the color of the cells the eraser is touching to white
        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                self.canvas.itemconfig(self.cells[i][j], fill="white")

# Create the main window and run the app
root = tk.Tk()
app = EraserApp(root)
root.mainloop()
