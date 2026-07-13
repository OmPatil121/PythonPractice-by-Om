class Calculator:
    def __init__(self,number):
        self.number = number
    def square(self):
        return  (self.number)**2
    def cube(self):
        return  (self.number)**3
    def root(self):
        return  (self.number)**0.5

c1 = Calculator(9)
print(c1.square())
print(c1.cube())
print(c1.root())

        
