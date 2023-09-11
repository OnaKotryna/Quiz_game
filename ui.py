from tkinter import *

THEME_COLOR = "#3753ff"
def set_false():
    pass

def set_true():
    pass

class QuizInterface():
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz app")
        self.window.config(padx=30, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 250/2, text="Question", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Ariel", 15, "bold"))
        self.score.grid(row=0, column=1)

        # Button to set answer as false
        img_false = PhotoImage(file="./images/false.png")
        btn_false = Button(image=img_false, highlightthickness=0, bd=0, command=set_false)
        btn_false.grid(row=2, column=0)

        # Button to set answer as true
        img_true = PhotoImage(file="./images/true.png")
        btn_true = Button(image=img_true, highlightthickness=0, bd=0, command=set_true)
        btn_true.grid(row=2, column=1)

        self.window.mainloop()
