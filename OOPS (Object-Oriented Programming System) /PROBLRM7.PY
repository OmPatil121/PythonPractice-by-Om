class library:
    def __init__(self):
        self.book = []
    def addbook(self,bookname):
        self.book.append(bookname)
        print("Book added")
    def searchbook(self,bookname):
        if bookname in self.book:
            print("Book found! ")
        else:
             print("Book not found! ")
    def showbook(self):
        print(self.book)
    def deletebook(self,dbook):
        if dbook in self.book:
            self.book.remove(dbook)
            print("Book removed ")

        else:
             print("Book not found! ")

        
li  = library()
li.addbook("harry potter")
li.addbook("the curse of letting go")
li.addbook("rich dad poor dad")
li.addbook("aginetra")
li.deletebook("harry potter")
li.showbook()
