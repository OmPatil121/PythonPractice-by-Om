class Animals:
    def __init__(self,type):
        self.type = type
    
class Pets(Animals):
    def __init__(self, name):
        super().__init__(type)
        self.name = name
        
class Dog(Pets):
    def __init__(self, type , name, breed):
        Pets.__init__(self,name)
        Animals.__init__(self,type)
        self.breed = breed 

    def bark(self):
        print(f"The pet owner own a {self.type} of breed {self.breed} and its name is {self.name}")
        print("Bhaow Bhaow")

d1 = Dog("Dog","mitra","bengali")
d1.bark()
