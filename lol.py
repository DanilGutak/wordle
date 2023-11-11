from wordle import check_letters
from wordle import choose_word
from wordle import check_guess
import tkinter as tk

class Wordle:
    j = 0
    word = "zoomy"
    i = 0

    def __init__(self, root):
        self.root = root
        self.root.title("Wordle")
        self.root.configure(bg="pink")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.frame1 = tk.Frame(root, bg="pink", width=350, height=600)
        self.frame1.pack(side=tk.TOP, fill=tk.Y)
        self.frame1.pack_propagate(False)

        self.entry = tk.Entry(self.frame1, validate="key", validatecommand=(root.register(self.validate_input), "%S", "%P"))
        self.entry.pack(pady=20)
        self.entry.focus_set()

        self.error_label = tk.Label(self.frame1, text="", font=("Arial", 17),fg = "red", bg="pink")
        self.error_label.pack()

        self.canvas = tk.Canvas(self.frame1, width=251, height=301, bg = "light blue")
        self.canvas.pack()
        self.row_curr = 0
        self.wordle_grid = [['' for _ in range(5)] for _ in range(6)]

        for row in range(6):
            for col in range(5):
                letter = ' '
                x1, y1 = col * 50 + 1, row * 50 + 1
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")

                text_x, text_y = (x1 + x2) / 2, (y1 + y2) / 2
                self.canvas.create_text(text_x, text_y, text=letter, font=("Arial", 30), fill="black")
        self.result_label = tk.Label(self.frame1, text="", font=("Arial", 20), bg="pink", fg = "green")
        self.result_label.pack(pady=20)
        self.root.bind("<Return>", lambda event: self.on_enter()) 
        self.root.bind("<Escape>", lambda event: root.destroy())
    
    def update_canvas(self, input_text):
            for col in range(5):
                letter = input_text[col]
                x1, y1 = col * 50 + 1, self.row_curr * 50 + 1
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")
                text_x, text_y = (x1 + x2) / 2, (y1 + y2) / 2
                self.canvas.create_text(text_x, text_y, text=letter, font=("Arial", 30), fill="black")
            self.row_curr += 1
            if self.row_curr == 6:
                self.row_curr = 0
                return True
            return False
        
    def on_enter(self):
        if(Wordle.j == 0 and Wordle.i == 0):
           Wordle.word = choose_word();
        Wordle.i = 0
        input_text = self.entry.get()
        if len(input_text) < 5 or check_guess(input_text) == -1:
            Wordle.i = 1
            self.error_label.config(text="Less than 5 chars or not a word!")
            return
        print(input_text)
        Wordle.j = check_letters(Wordle.word, input_text, Wordle.j)
        self.entry.delete(0, tk.END)
        self.update_canvas(input_text)
        self.error_label.config(text="")
    def validate_input(self, char, text):
        if len(text) > 5:
            return False
        elif not char.isalpha():
            return False
        elif not char.isascii():
            return False
        return True

def main():
    root = tk.Tk()
    Wordle(root)
    root.mainloop()

if __name__ == "__main__":
    main()