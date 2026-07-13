class car:
    def __init__(self,brand,speed):
                 self.brand = brand
                 self.speed = speed
    def show_info(self):
        print(f"Brand : {self.brand}")
        print(f"Speed : {self.speed}")
    def acc(self,inc):
           self.speed = self.speed + inc
           print(f"New speed is {self.speed}")

c1 = car("toyoya",120)
c1.acc(40)
c1.show_info()
