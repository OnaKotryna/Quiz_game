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
        if question.answer.lower() == user_answer.lower() or question.answer[0].lower() == user_answer[0].lower():
            self.score += 1
            self.questions[self.questions.index(question)].guessed = True
        else:
            self.questions[self.questions.index(question)].guessed = False

    def have_question(self):
        return self.question_num < len(self.questions)
