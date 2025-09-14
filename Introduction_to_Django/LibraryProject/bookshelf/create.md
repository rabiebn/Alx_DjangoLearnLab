from bookshelf.models import Book

book = Book(title='1984', author='George Orwell', publication_year=1949)
book.save()
print(f"Book Created: {book.title} by {book.author} in {book.publication_year}")

`Book Created: 1984 by George Orwell in 1949`