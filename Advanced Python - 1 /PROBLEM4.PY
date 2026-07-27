a : int = int(input("A: "))
b : int = int(input("B: "))

if b==0:
    raise ZeroDivisionError("infinite")
    
else:
    print(a+b)

