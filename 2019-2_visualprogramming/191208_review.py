class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result = self.result + num
        return self.result


class SuperCalculator(Calculator):
    def subtractor(self, num):
        self.result = self.result - num
        return self.result


cal = Calculator()
