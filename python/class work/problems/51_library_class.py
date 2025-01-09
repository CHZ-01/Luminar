# Define a class called Book with attributes: title, author, year

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def get_summary(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year_published}")

book1 = Book("1984","George Orwell",1949)
book1.get_summary()