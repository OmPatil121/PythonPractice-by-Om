user_input = int(input("Wrtie a number here: "))
l2 = [user_input*i for i in range(1,11)]

with open("table.txt","w") as f:
    for i  in l2:
        content = f.write(f"{str(i)}\n")
    
    
