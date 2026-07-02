with open("digit.txt","w") as f:
    text = f.write('''1
2
3
4
5
6
7
8
9
11''')

with open("digit.txt") as k:
    content = k.readlines()
def sum():
    z = 0
    for i in content:
        z +=  int(i.strip())
    return z
                
print(sum())
