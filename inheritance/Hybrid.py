class Apple:
    def __init__(self,books):
        self.books=books
       

class meesho(Apple):
    def __init__(self,fashion):
        self.fashion=fashion

class bookswagon(Apple):
    def __init__(self,books):
        super().__init__(books)
        print("flipcark provide products like",{self.books},"same as apple")

class flipcart(meesho,bookswagon):
    def __init__(self,fashion,books):
        meesho.__init__(self,fashion)
        bookswagon.__init__(self,books)
    
    def provide(self):
        print("flipcart provide",{self.books},"and also",{self.fashion})


obj=flipcart("fashion","books")
obj.provide()