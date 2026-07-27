li = [i for i in range(0,101)]

def sort(n):
    if n%5 == 0:
        return True
    return False


val = list(filter(sort,li))
print(val)
