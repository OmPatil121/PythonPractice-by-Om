class fly:
    @staticmethod
    def fly():
        print("I can Fly")

class swim:
    @staticmethod
    def swim():
        print("I can swim")
    
class duck(fly,swim):
    @staticmethod
    def quack():
        print("Quack Quack")

d1 = duck()
d1.swim()
d1.fly()
d1.quack()
