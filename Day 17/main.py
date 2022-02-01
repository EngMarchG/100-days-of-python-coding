from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    questionHolder = question["text"]
    questionAnswer = question["answer"]
    new_question = Question(questionHolder, questionAnswer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_score()