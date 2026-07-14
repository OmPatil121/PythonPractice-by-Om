class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg(self):
        z = 0
        for i in self.marks:
            z += i
        return  z/len(self.marks)
                
    def grade(self):
        if self.avg() >= 90:
            print(f"You got A with percentage {self.avg()}%")

        elif self.avg() >=75 and self.avg() <=89:
            print(f"You got B  percentage {self.avg()}%")

        elif self.avg() >=60 and self.avg() <=74:
            print(f"You got C  percentage {self.avg()}%")

        else:
            print(f"You got F  percentage {self.avg()}%")

s1 = Student("Om",[90,90,90,90,90])
print(s1.avg())
s1.grade()

    
