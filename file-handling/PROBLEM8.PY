with open("story.txt","w") as f:
    text = f.write('''The sun was setting over the mountains.
A young boy was sitting by the river alone.
He was thinking about his future and his dreams.
Suddenly a bird landed near him and sang a song.
The boy smiled and felt hopeful again.''')

with open("story.txt") as k:
    content = k.readlines()
    z = []    
    for line in content:
        z.append(line) 


with open("story.txt") as x: 
    y = []
    war = x.read()
    for words in war.split():
        y.append(words)

w = len(y)
l = len(z)
print(f"In story file there are {w} words and {l} line")
