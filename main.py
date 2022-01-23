from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []
for dict in question_data:
    questions = Question(dict['text'], dict['answer'])
    questionBank.append(questions)

quiz=QuizBrain(questionBank)

while quiz.questionsStill():
    quiz.nextQuestion()