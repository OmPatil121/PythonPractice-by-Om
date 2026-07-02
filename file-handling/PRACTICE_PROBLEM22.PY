with open("fruits.txt","w") as f:
    text = f.write('''apple
banana
mango
grapes
orange''')
with open("fruits.txt") as k:
    content = k.readlines()
    for i in content:
        if len(i.strip()) > 5:
            print(i.strip())
            
        
            