class QuizBrain:
    def __init__(self, questionList):
        self.number = 0
        self.list = questionList

    def nextQuestion(self):
        currentQuestion = self.number
        self.number += 1
        input(f'Q.{self.number}: {self.list[currentQuestion].text} (True/False):\n')


    def questionsStill(self):
        return len(self.list) > self.number