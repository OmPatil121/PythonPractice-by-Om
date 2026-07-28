from functools import reduce
l = [1,2,35,6,3]

def greater(a,b):
    if a > b:
        return a 
    return b 

l = reduce(greater,l)
print(l)
