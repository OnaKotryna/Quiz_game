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
            self.questions[question].guessed = True
        else:
            self.questions[question].guessed = False

    def has_question(self):
        return self.question_num < len(self.questions)
