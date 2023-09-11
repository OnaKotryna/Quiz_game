from data import load_questions
from game import Game
import os

from ui import QuizInterface


game = Game(load_questions())
quiz_ui = QuizInterface(game)
