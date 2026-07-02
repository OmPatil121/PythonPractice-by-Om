with open("students.txt" , "w") as f:
    text = f.write('''Om
Rahul
Priya
Arjun
Sneha''')

with open("students.txt" ) as k:
    content = k.readlines()    

def search_student(n):
    for i in content:
        if i.strip() == n:
            print(f"{n} found in file")
            break
    else:
        print(f"{n} not found in file")
            
search_student("Sneha")
