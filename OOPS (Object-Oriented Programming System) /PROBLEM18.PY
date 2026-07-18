class Employee:
    def __init__(self,salary):
        self.salary = salary
class Increment(Employee):
    def __init__(self, salary , Increment):
        super().__init__(salary)
        self.Increment = Increment
    def final_salary(self):
        print(f"The previous salary was {self.salary} and you got increment of {self.Increment}. So, your new salary is {self.salary + self.Increment}")

e1 = Increment(1200,1000)
e1.final_salary()
