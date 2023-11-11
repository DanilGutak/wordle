from wordle import choose_word
from wordle import check_guess
from wordle import search_letter
import tkinter as tk

class Wordle:
    j = 0
    word = "zoomy"
    i = 0
    answer = list("00000")

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
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="yellow" if self.answer[col] == 'y' else "green" if self.answer[col] == 'g' else "white")

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
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black" ,fill="yellow" if self.answer[col] == 'y' else "green" if self.answer[col] == 'g' else "white")
                text_x, text_y = (x1 + x2) / 2, (y1 + y2) / 2
                self.canvas.create_text(text_x, text_y, text=letter, font=("Arial", 30), fill="black")
            self.row_curr += 1
            if self.row_curr == 6:
                self.row_curr = 0
                return True
            return False

    def check_letters(self,  input_text):
        guess = input_text
        answer = list("00000")
        i = 0
        print(self.word)
        while(i < 5):
            search_letter(self.word, guess[i], i, answer)
            i+=1
        self.answer = answer
        print(self.answer)
        self.j+=1
        if(self.j == 6):
            self.j = 0
        if self.answer == list("ggggg"):
            self.result_label.config(text="You win!")
            self.entry.config(state="disabled")
            self.root.unbind("<Return>")
        return(False)

    def on_enter(self):
        if(self.j == 0 and self.i == 0):
            self.word = choose_word()
        self.i = 0
        input_text = self.entry.get()
        if input_text == "":
            self.i = 1
            return
        if len(input_text) < 5 or check_guess(input_text) == -1:
            self.i = 1
            self.error_label.config(text="Not a correct word!")
            return
        self.check_letters(input_text)
        self.entry.delete(0, tk.END)
        if self.update_canvas(input_text) == True:
            self.result_label.config(text="You lose!")
            self.entry.config(state="disabled")
            self.root.unbind("<Return>")
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