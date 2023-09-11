from tkinter import *
from game import Game

THEME_COLOR = "#3753ff"


class QuizInterface():
    def __init__(self, game: Game):
        self.game = game

        self.window = Tk()
        self.window.title("Quiz app")
        self.window.config(padx=30, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 250/2, text="Question", font=("Arial", 18, "italic"), width=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Ariel", 15, "bold"))
        self.score.grid(row=0, column=1)

        # Button to set answer as false
        img_false = PhotoImage(file="./images/false.png")
        btn_false = Button(image=img_false, highlightthickness=0, bd=0, command=self.set_false)
        btn_false.grid(row=2, column=0)

        # Button to set answer as true
        img_true = PhotoImage(file="./images/true.png")
        btn_true = Button(image=img_true, highlightthickness=0, bd=0, command=self.set_true)
        btn_true.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.game.has_question():
            question = self.game.get_question()
            self.canvas.itemconfig(self.question, text=f"Q{self.game.question_num}: {question.question}")
        else:
            self.canvas.itemconfig(self.question, text=f"Game Over\nScore: {self.game.score}")
            self.canvas.config(bg=THEME_COLOR)
        

    def set_false(self):
        self.set_answer("false")

    def set_true(self):
        self.set_answer("true")

    def set_answer(self, answer):
        if self.game.check_answer(self.game.question_num, answer):
            self.canvas.config(bg="#90EE90")
        else:
            self.canvas.config(bg="#FF6961")
        self.score.config(text=f"Score: {self.game.score}")
        self.window.after(1000, self.get_next_question)
