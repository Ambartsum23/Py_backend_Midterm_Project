class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

class BookManager:
    def __init__(self):
        self.books = []
        self.dictionary = {}

    def add_book(self, book):
        self.books.append(book)
        self.dictionary[book.title] = book

    def get_book(self, title):
        return self.dictionary.get(title)

    def get_books(self):
        books = ""
        for book in self.books:
            books += str(book)
            books += ','
            books += '\n'
        return books

def main():
    manager = BookManager()
    while True:
        action = input("""tell us what you whant to do:
            1. add book
            2. get book
            3. get list of books
            4. exit 
tipe action number: """)
        if action == "1":
            name = input("Enter book name: ")
            author = input("Enter book author: ")
            while True:
                try:
                    year = int(input("Enter book year: "))
                    break
                except ValueError:
                    print("Enter a valid book year")
            book = Book(name, author, year)
            manager.add_book(book)
            print("book added")

        elif action == "2":
            book_title = input("Enter book name: ")
            print(manager.get_book(book_title))

        elif action == "3":
            print(manager.get_books())

        elif action == "4":
            print("goodbye")
            break

        else:
            print("Enter a valid action")

main()


