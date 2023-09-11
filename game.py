class Game:
    def __init__(self, questions):
        self.score = 0
        self.question_num = 0
        self.questions = questions

    def get_question(self):
        question = self.questions[self.question_num]
        self.question_num += 1
        return question

    def check_answer(self, question, user_answer):
        question = int(question) - 1
        if self.questions[question].answer.lower() == user_answer.lower():
            self.score += 1
            checked = True
        else:
            checked = False
        self.questions[question].guessed = checked 
        return checked

    def has_question(self):
        return self.question_num < len(self.questions)

    def reset(self):
        self.score = 0
        self.question_num = 0
