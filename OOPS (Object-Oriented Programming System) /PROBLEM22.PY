class Volume:
    def __init__(self,l,b,h):
        self.l = l
        self.b = b
        self.h = h

    def vol(self):
        return self.l * self.b * self.h
    
    def __lt__(self, other):
        return self.vol() < other.vol()
        
    def __gt__(self, other):
        return self.vol() > other.vol()
    
c1 = Volume(100,2,3)
c2 = Volume(4,5,6)
c3 = c1<c2
print(c3)
        
