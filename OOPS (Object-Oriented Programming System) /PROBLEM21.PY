class Complex:
    def __init__(self,r,i):
        self.i = i
        self.r = r
    
    def __mul__(self, other):
        newi = (self.r * other.i) + (self.i * other.r)
        newr = (self.r * other.r) - (self.i*other.i)
        return Complex(newr, newi)
        
    def __str__(self):
        return f"Your complex number is {self.r} + {self.i}i"
    
c1 = Complex(-1,2)
c2 = Complex(2,2)
c3 = c1 * c2
print(c3)
