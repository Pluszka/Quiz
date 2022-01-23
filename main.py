from question_model import Question
from data import question_data, newQuestions
from quiz_brain import QuizBrain

questionBank = []
# for dict in question_data:
#     questions = Question(dict['text'], dict['answer'])
#     questionBank.append(questions)

for dict in newQuestions:
    questions = Question(dict['question'], dict['correct_answer'])
    questionBank.append(questions)

quiz=QuizBrain(questionBank)

while quiz.questionsStill():
    quiz.nextQuestion()

print(f'You finished the quiz! \nYour final score is equal {quiz.score}/{len(questionBank)} ')