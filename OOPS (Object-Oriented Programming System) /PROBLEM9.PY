class animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        pass
class dog(animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("woof",self.name)

class cat(animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("meow",self.name)

class cow(animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("moo",self.name)

d1 = dog("Tommy")
d1.speak()

c1 = cat("Kitty")
c1.speak()

co1 = cow("Daisy")
co1.speak()
