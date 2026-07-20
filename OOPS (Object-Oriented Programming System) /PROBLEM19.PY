class Circle:
    def __init__(self,radius):
        self._radius = 0
        self.radius = radius
    
    @property
    def radius(self):
        print("s")
        return self._radius 
        
    
    @radius.setter
    def radius(self, value):  
        if value < 0:
            print("Invalid radius")  
        else:
            self._radius = value
    def area(self):
        print(3.14 * self._radius *self._radius)

c1 = Circle(-2)
c1.radius = -5
c1.area()
