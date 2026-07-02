
with open("text.txt","w") as f:
      text = f.write('''name is Om.
I am learning Python.
I want to become an AI engineer''')

with open("text.txt") as k:
      test = k.read()
      print(test)
