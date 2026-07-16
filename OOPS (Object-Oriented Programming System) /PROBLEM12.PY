class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
class employee:
    def __init__(self,company,salary):
        self.company = company
        self.salary = salary
    
class manager(person,employee):
    def __init__(self, name, age,company,salary):
        person.__init__(self,name, age)
        employee.__init__(self,company,salary)
    def intro(self):
        print(f"Name = {self.name} \n age = {self.age} \n company = {self.company} \n salary = {self.salary}")

e1  = manager("om",21,"Google",12000000)
e1.intro()
        
        
