# Including a book into the library records
class Book:
    book_title = ""
    author = ""
    year_of_publication = 0
    def __init__(self, book_title, author, year_of_publication):
        self.book_title = book_title
        self.author = author
        self.year_of_publication = year_of_publication

    def get_book_title(self):
        return self.book_title

    def get_author(self):
        return self.author

    def get_year_of_publication(self):
        return self.year_of_publication

    def set_book_title(self, book_title):
        self.book_title = book_title

    def set_author(self, author):
        self.author = author

    def set_year_of_publication(self, year_of_publication):
        self.year_of_publication = year_of_publication

    def __str__(self):
        return "Book Title:" + "\t"+self.book_title + "\n" + "The Author:" +"\t" + self.author + "\n" +"Year of Publication:" + "\t" + str(self.year_of_publication)

NewBook = Book("Programming", "Wangechy J.T", 2021)
print( "The initial values of the NewBook function")
print(NewBook)

NewBook.set_book_title("Cooking")
NewBook.set_author("Jatavia J.T")
NewBook.set_year_of_publication(2020)

print("\n")
print("The new values of the NewBook function")
print(NewBook )
