from words import choose_word
from words import check_guess
from words import search_letter
import tkinter as tk
from PIL import Image, ImageTk

class Wordle:
    j = 0
    word = ""
    i = 0
    answer = list("00000")
    win_flag = False
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle")
        self.root.configure(bg="pink")
        self.root.geometry("400x800")
        self.root.resizable(False, False)
        self.image = tk.PhotoImage(file='caticon.png')
        self.root.iconphoto(False, self.image)
        self.image_item = None
        self.image_item2 = None
        self.image_item3 = None
        self.image_item4 = None


        self.frame1 = tk.Frame(root, bg="pink", width=350, height=750)
        self.frame1.pack(side=tk.TOP, fill=tk.Y)
        self.frame1.pack_propagate(False)

        self.entry = tk.Entry(self.frame1, validate="key", validatecommand=(root.register(self.validate_input), "%S", "%P"))
        self.entry.pack(pady=20)
        self.entry.focus_set()

        self.error_label = tk.Label(self.frame1, text="", font=("Montserrat", 17),fg = "red", bg="pink")
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
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
                text_x, text_y = (x1 + x2) / 2, (y1 + y2) / 2
                self.canvas.create_text(text_x, text_y, text=letter, font=("Arial", 30), fill="black")

        self.result_label = tk.Label(self.frame1, text="", font=("Arial", 16), borderwidth=0, bg="pink", fg = "green")
        self.result_label.pack(pady=20)

        self.original_image = Image.open("cat.png")
        self.tk_image = ImageTk.PhotoImage(self.original_image)
        self.vic_canvas = tk.Canvas(self.frame1, width=500, height=350, borderwidth=0, bg = "pink", highlightthickness=0)
        self.vic_canvas.pack()

        self.root.bind("<Return>", lambda event: self.on_enter()) 
        self.root.bind("<Escape>", lambda event: root.destroy())
    

    def spin_image(self, angle=0):
        rotated_image = self.original_image.rotate(angle)
        self.tk_image = ImageTk.PhotoImage(rotated_image)
        self.vic_canvas.itemconfig(self.image_item, image=self.tk_image)
        self.vic_canvas.itemconfig(self.image_item4, image=self.tk_image)

        self.vic_canvas.itemconfig(self.image_item2, image=self.tk_image)
        self.vic_canvas.itemconfig(self.image_item3, image=self.tk_image)
        if angle > 1080:
            return

        self.root.after(100, lambda: self.spin_image(angle + 35 ))

    def update_canvas(self, input_text):
            for col in range(5):
                letter = input_text[col].upper()
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

    def restart(self):
        self.vic_canvas.delete(self.image_item)
        self.vic_canvas.delete(self.image_item2)
        self.vic_canvas.delete(self.image_item3)
        self.vic_canvas.delete(self.image_item4)
        self.canvas.delete("all")
        self.canvas.pack()
        self.row_curr = 0
        self.wordle_grid = [['' for _ in range(5)] for _ in range(6)]
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.focus_set()
        self.error_label.config(text="")
        self.result_label.config(text="")
        self.j = 0
        self.root.bind("<Return>", lambda event: self.on_enter())
        for row in range(6):
            for col in range(5):
                letter = ' '
                x1, y1 = col * 50 + 1, row * 50 + 1
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
                text_x, text_y = (x1 + x2) / 2, (y1 + y2) / 2
                self.canvas.create_text(text_x, text_y, text=letter, font=("Arial", 30), fill="black")

    def check_letters(self,  input_text):
        guess = list(input_text)
        answer = list("00000")
        i = 0
        search_letter(list(self.word), answer, guess)
        #print(self.word)
        self.answer = answer
        self.j+=1
        if self.answer == list("ggggg"):
            self.result_label.config(text="You win!\n" +"You managed to do it in " +str(self.j) + " guesses.\n" +"Press Enter to restart...", fg = "green")
            self.image_item = self.vic_canvas.create_image(-50, -50, anchor=tk.NW, image=self.tk_image)
            self.image_item2 = self.vic_canvas.create_image(-30, 70, anchor=tk.NW, image=self.tk_image)
            self.image_item3 = self.vic_canvas.create_image(100, -50, anchor=tk.NW, image=self.tk_image)
            self.image_item4 = self.vic_canvas.create_image(120, 60, anchor=tk.NW, image=self.tk_image)
            self.spin_image()
            self.entry.config(state="disabled")
            self.root.unbind("<Return>")
            self.win_flag = True
            self.root.bind("<Return>", lambda event: self.restart())
        if(self.j == 6):
            self.j = 0
        return(False)

    def on_enter(self):
        if(self.j == 0 and self.i == 0):
            self.word = choose_word()
        self.i = 0
        input_text = self.entry.get()
        input_text = input_text.lower()
        if input_text == "":
            self.i = 1
            return
        if len(input_text) < 5  or check_guess(input_text) == -1:
            self.i = 1
            self.error_label.config(text="Not a dictionary word!")
            return
        self.check_letters(input_text)
        self.entry.delete(0, tk.END)
        if self.update_canvas(input_text) == True and self.win_flag == False: 
            self.result_label.config(text="You lose! \n The word was " + self.word.upper() + ".\n " + "Press Enter to restart...", fg = "red")
            self.entry.config(state="disabled")
            self.root.unbind("<Return>")
            self.root.bind("<Return>", lambda event: self.restart())
        self.error_label.config(text="")
        self.win_flag = False
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