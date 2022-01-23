class QuizBrain:
    def __init__(self, questionList):
        self.number = 0
        self.list = questionList

    def nextQuestion(self):
        input(f'{self.number}: {self.list[self.number]} (True/False):\n')