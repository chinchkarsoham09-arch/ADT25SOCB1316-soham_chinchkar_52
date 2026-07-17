class library:
    def __init__(self):
        self.books=[]
        self.patrons=[]
    def add_book(self,book):
        book=input("enter the book ")
        self.books.append(book)
    def add_patrons(self,patron):
        patron=input("enter the patron")
        self.patrons.append(patron)
    def display_book(self):
        print("available books:",self.books)
    def display_patrons(self):
        print("available books:",self.patrons)
lib=library()
lib.add_book()
lib.add_book()
lib.display_book()
lib.display_patrons()
while(True):
    print("\n1.add_book")
    print("\n2.add_patorn" )
    print("\n3.display all books ")
    print("\n4.display all patrons" )
    print("\n5.end")
    ch=input("enter your ch")
    if(ch==1):
        lib.add_book()
    elif(ch==2):
        lib.add_patrons()
    elif(ch==3):
        lib.display_book()
    elif(ch==4):
        lib.display_patrons()
    elif(ch==5):
        break