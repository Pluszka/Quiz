class QuizBrain:
    def __init__(self, questionList):
        self.number = 0
        self.list = questionList
        self.promptingNum = self.number + 1

    def nextQuestion(self):
        input(f'{self.promptingNum}: {self.list[self.number].text} (True/False):\n')