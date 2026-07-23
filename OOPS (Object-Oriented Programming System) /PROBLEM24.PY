class Shoopingcart:
    def __init__(self,items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self,index):
        return self.items[index]

c1 = Shoopingcart(['apple','banana','orange'])
print(len(c1))
print(c1[1:3])
print(c1[2])
print(c1[1])
        
