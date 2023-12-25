from question_model import Question
from data import question_data
from quiz_brain import *

question_bank = []

for data in question_data:
    question = Question(data["text"], data["answer"])
    question_bank.append(question)

start = Brain(question_bank)

while start.still_have_question():
    start.next_question()