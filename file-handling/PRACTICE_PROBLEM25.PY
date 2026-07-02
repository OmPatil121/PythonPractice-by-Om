with open("Dairy.txt","w") as f:
    text = f.write("Hey dear dairy today is 3/jul/2026 \n")
with open("Dairy.txt","a") as k:
    content = k.write("Hey dear dairy today is 4/jul/2026 \n")
with open("Dairy.txt","a") as l:
    test = l.write("Hey dear dairy today is 5/jul/2026 ")
with open("Dairy.txt") as c:
    read = c.read()
    print(read)

