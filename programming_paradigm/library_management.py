class Book:
    """Represents a single book with title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it’s available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available (returned)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available, False if checked out."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages a collection of Book objects."""

    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        """Add a new Book object to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title, if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """Print all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
