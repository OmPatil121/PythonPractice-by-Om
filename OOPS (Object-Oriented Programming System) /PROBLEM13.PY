class animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")
        
class domestic:
    def __init__(self,owner):
        self.owner = owner
    def pet(self):
        print(f"{self.name} is pet of {self.owner} and he is {self.age} year old ")

class dog (animal,domestic):
    def __init__(self, name, age,owner):
        animal.__init__(self,name, age)
        domestic.__init__(self,owner)
    def fetch(self): 
        print(f"{self.name} fetched the ball!")
    @staticmethod
    def woof():
        print("woof!")
        
d1 = dog("ABhi",2,"OM")
d1.fetch()
d1.woof()
d1.pet()
d1.eat()
