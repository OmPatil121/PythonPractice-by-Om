class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self, other):
        newi  = self.i + other.i
        newj = self.j + other.j
        newk  = self.k + other.k
        return Vector(newi,newj,newk)
        
    def __mul__(self, other):
        new_i  = self.i * other.i
        new_j = self.j * other.j
        new_k  = self.k * other.k
        return new_i+new_j+new_k
    def __str__(self):
        return f"{self.i}i+{self.j}k+{self.k}k"
    
c1 = Vector(1,-2,3)
c2 = Vector(4,5,6)
c3 = c1+c2
c4 = c1*c2

print(c3,c4)
