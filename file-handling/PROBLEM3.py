with open("numbers.txt", "w") as f:
    for i in range(1,11):
        content = f.write(f"{i}\n")
with open("numbers.txt") as k:
    text= k.read()
    print(text)
