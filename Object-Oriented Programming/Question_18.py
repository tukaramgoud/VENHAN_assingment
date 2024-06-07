'''18. Create a class Book with the following attributes and methods:
*Attributes: `title`, `author`, `pages`
*Methods:
*`__init__(self, title: str, author: str, pages: int)`: Constructor to initialize the attributes.
*`__str__(self) -> str`: Method to return a string representation of the book.
'''

class Book():
    def __init__(self,title, author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return("{} this book is writen by {} contain {} pages".format(self.title, self.author, self.pages))


book_1 = Book("Secret", "Rhonda Brine", 92)
print(book_1.__str__())