class Add:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self, other):  
        new_r = self.r + other.r
        new_i = self.i + other.i
        return Add(new_r, new_i)  

        
    def __str__(self):
        return f"Your complex no. is {self.r} + {self.i}i"

c1 = Add(2, 3)
c2 = Add(1, 4)
c3 = c1 + c2  
print(c3)     
