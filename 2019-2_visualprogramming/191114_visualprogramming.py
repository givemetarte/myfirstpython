class Calculator:
    def __init__(self):
        print("init")
        self.result = 0

    def adder(self,num):
        print("adder")
        self.result = self.result + num
        return self.result
    print("program start")

    print("cal1 create")
    cal1 = Calculator()
    print("cal2 create")
    cal2 = Calculator()

    print("method start")
    print(cal1.adder(3))
    print(cal1.adder(4))
    print(cal2.adder(3))
    print(cal2.adder(7))
