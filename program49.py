
class Publisher:
    def __init__(self,name):
        self.name=name

class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author

class Python(Book):
    def __init__(self,name,title,author,price,pages):
        super().__init__(name,title,author)
        self.price=price
        self.pages=pages

    def display(self):
        print("\nPython Book Details")
        print("Publisher:",self.name)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)
        print("Number of pages:",self.pages)


p = Python("DC Publications","Python Programming","Anna",1550,500)
p.display()
