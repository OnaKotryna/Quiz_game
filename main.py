from data import load_questions
from game import Game
import os

from ui import QuizInterface


game = Game(load_questions())
quiz_ui = QuizInterface(game)

# while game.have_question():
#     question = game.get_question()
#     if question:
#         answ = input(
#             f"Q{game.question_num}: {question.question} True or False? \n")
#         game.check_answer(question, answ)

# print('*******************************')
# print(f'Your score: {game.score}/{game.question_num} ')
# print('Answers:')
# num = 1
# for q in game.questions:
#     print(f'Q{num}: {q.question}')
#     num += 1
#     if q.guessed:
#         print(f'Correct. Answer: {q.answer}')
#     else:
#         print(f'Incorrect. Answer: {q.answer}')
#     print('*******************************')
