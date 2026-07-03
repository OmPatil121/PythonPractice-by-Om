l1 = "Om 85" #["om" ,"85"]
l2 = "Rahul 72"
l3 = "Priya 90"
l4 = "Arjun 65"
l5 = "Sneha 78"

with open("marks.txt","w") as f:
    text = f.write(f"{l1}\n{l2}\n{l3}\n{l4}\n{l5}")

with open("marks.txt") as k:
        content = k.readlines()
        for i in content:
            z =   i.strip()
            j = z.split()
            if int(j[1]) > 75:
                 print(z)
                 



