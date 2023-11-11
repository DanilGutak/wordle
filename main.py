import tkinter as tk

def delete_label():
    # Destroy the label widget
    text_label.destroy()
def validate_input(char, current_text):
    # Only allow up to 5 letters
    return len(current_text) < 6 and char.isalpha() and char.isascii()
def on_enter(entered_data, entry, frame2):
    entered_data.set(entered_data.get())
    if len(entered_data.get()) < 5:
        text_label.config(text="Less than 5 chars!", fg="red")
        return
    text_label.config(text="")
    print(f"Entered data: {entered_data.get()}")
    entry.delete(0, tk.END)

def main():

    global text_label
    root = tk.Tk()
    root.title("Wordle") # Set the title of the window
    
    # Set the initial size of the window
    root.geometry("600x400") # Width x Height
    root.resizable(False, False) # Disable resizing in both directions

    frame1 = tk.Frame(root, bg="lightgray", bd=5, width=180, height=400)
    frame1.pack(side=tk.LEFT, fill=tk.Y)
    frame1.pack_propagate(False) # Prevent the frame to resize to the labels size
    # Create a Label widget with customized text and styling
    frame2 = tk.Frame(root, bg="lightgray", bd=5, width=180, height=400)
    frame2.pack(side=tk.LEFT, fill=tk.Y)
    frame2.pack_propagate(False)
    # Pack the Label widget to make it visible in the window
    entered_data = tk.StringVar()
    entry = tk.Entry(frame2, textvariable=entered_data ,validate="key", validatecommand=(root.register(validate_input), "%S", "%P"))
    entry.pack(pady=20)
    entry.focus_set()

    text_label = tk.Label(frame2, text="", font=("Arial", 10), bg="lightgray")
    text_label.pack()

    root.bind("<Escape>", lambda event: root.destroy())
    entry.bind("<Return>", lambda event:on_enter(entered_data, entry, frame2))

    rows, cols = 6, 5
    cell_size = 50

    # Create a canvas
    canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size, bg="white")
    canvas.pack()

    # Create a 2D list to store letters in the grid
    wordle_grid = [['' for _ in range(cols)] for _ in range(rows)]

    # Populate the grid with letters (you can replace this with your own logic)
    for row in range(rows):
        for col in range(cols):
            letter = chr(ord('A') + (row * cols + col) % 26)  # Just an example, replace with your logic
            wordle_grid[row][col] = letter

            # Draw rectangles for each cell
            x1, y1 = col * cell_size, row * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, outline="black")

            # Draw text (letter) in the center of each cell
            text_x, text_y = (x1 + x2) / 2, (y1 + y2) / 2
            canvas.create_text(text_x, text_y, text=letter, font=("Arial", 12), fill="black")

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

