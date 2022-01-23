class QuizBrain:
    def __init__(self, questionList):
        self.number = 0
        self.list = questionList
        self.score = 0

    def nextQuestion(self):
        currentQuestion = self.number
        self.number += 1
        userAnswer=input(f'Q.{self.number}: {self.list[currentQuestion].text} (True/False)?:\n')
        self.checkAnswer(userAnswer, self.list[currentQuestion].answer)

    def questionsStill(self):
        return len(self.list) > self.number

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            print('You scored a point!')
            self.score += 1
        else:
            print('You faild.')
        print(f'Your current score is {self.score}/{self.number}')