import requests
from question import Question
import json

params = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(
    "https://opentdb.com/api.php", params=params)
data = json.loads(response.text)['results']
# 12 - music


def load_questions():
    return [Question(q["question"], q["correct_answer"]) for q in data]
