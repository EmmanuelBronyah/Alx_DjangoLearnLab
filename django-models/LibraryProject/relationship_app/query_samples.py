from .models import Book, Author, Library, Librarian

# Query all books by a specific author.
author_name = "John Doe"
author = Author.objects.get(name=author_name)
books = author.book.all()

# List all books in a library.
books = Library.book.all()

# Retrieve the librarian for a library
librarian_name = "John Doe"
librarian = Library.librarian.get(name=librarian_name)