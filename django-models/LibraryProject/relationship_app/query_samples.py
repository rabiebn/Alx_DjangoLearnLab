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
library = Library.objects.get(name=library_name)
books = library.books.all()

#Retrieve the librarian for a library
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
