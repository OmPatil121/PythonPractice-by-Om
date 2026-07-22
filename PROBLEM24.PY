class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def __eq__(self, other):
        return self.roll_no == other.roll_no

    def __str__(self):
        return f"Name = {self.name} \n Roll_no = {self.roll_no}"

s1 = Student("Om", 12)
s2 = Student("keshave", 13)

print(s1 == s2)
print(s1)
