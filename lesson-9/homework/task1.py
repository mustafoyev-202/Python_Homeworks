class BookNotFoundException(Exception):
    """Exception raised when a book is not found in the library."""

    pass


class BookAlreadyBorrowedException(Exception):
    """Exception raised when a book is already borrowed."""

    pass


class MemberLimitExceededException(Exception):
    """Exception raised when a member tries to borrow more than the allowed limit of books."""

    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(
                f"{self.name} has already borrowed 3 books."
            )
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(
                f"The book '{book.title}' is already borrowed."
            )
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.return_book(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"The book '{title}' was not found in the library.")

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        raise Exception(f"Member '{name}' not found.")


# Test the program
library = Library()

# Adding books
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Adding members
member1 = Member("Alice")
member2 = Member("Bob")
library.add_member(member1)
library.add_member(member2)

# Borrowing books
try:
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "The Great Gatsby")
    library.borrow_book(
        "Alice", "Nonexistent Book"
    )  # This should raise BookNotFoundException
except Exception as e:
    print(e)

# Returning books
try:
    library.return_book("Alice", "1984")
    library.borrow_book("Alice", "1984")
except Exception as e:
    print(e)

# Handling exceptions
try:
    library.borrow_book("Bob", "1984")  # This should raise BookAlreadyBorrowedException
except Exception as e:
    print(e)

try:
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "The Great Gatsby")
    library.borrow_book(
        "Alice", "Another Book"
    )  # This should raise MemberLimitExceededException
except Exception as e:
    print(e)
