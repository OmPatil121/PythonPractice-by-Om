class TwoD_vector:
    def __init__(self,i,j ):
        self.i =i 
        self.j = j

class Three_Dvector(TwoD_vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def print(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

c1 = three(1,2,3)
c1.print()

