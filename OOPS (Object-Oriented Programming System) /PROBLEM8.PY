class shape:
    def __init__(self,color):
        self.color = color
    

class circle(shape):
    def __init__(self,radius,color):
        super().__init__(color)
        self.radius = radius
    def area(self):
        
        print(3.14*(self.radius**2))
    
class reactangle(shape):
    def __init__(self,length,breadth,color):
         self.length = length
         self.breadth = breadth
         super().__init__(color)
    def area(self):
        
       
        print(self.length*self.breadth)
    
c1 = reactangle(12,12,"blue")
c1.area()
