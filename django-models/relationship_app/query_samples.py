from .models import Book, Author, Library, Librarian

# Query all books by a specific author.
author_name = "John Doe"
books = Book.objects.filter(author=author)

# List all books in a library.
books = Library.objects.get(name=library_name)
books.all()

# Retrieve the librarian for a library
librarian_name = "John Doe"
librarian = Library.librarian.get(name=librarian_name)