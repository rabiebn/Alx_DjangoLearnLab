from .models import Book, Author, Library, Librarian

#Samples to work with
author1 = Author(name="J. K. Rowling")
book = Book(title="Harry Potter", author=author1.name)
lib = Library(name="City Library", books=[])
librarian = Librarian(name="Mohammed", library=lib)

#Query all books by a specific author
books_by_author = Book.objects.filter(author=author1)

#List all books in a library
library_name = lib.name
all_books_in_lib = Library.objects.get(name=library_name)

#Retrieve the librarian for a library
librarian = Librarian.objects.filter(library=lib.name)
