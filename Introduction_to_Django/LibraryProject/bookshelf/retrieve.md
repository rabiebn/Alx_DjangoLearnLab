from bookshelf.models import Book

retrieved_book = Book.objects.get(id=1)
print(f"Book Retrieved: {retrieved_book.title} by {bretrieved_bookook.author} in {retrieved_book.publication_year}")
`Book Retrieved: 1984 by George Orwell in 1949`

retrieved_book = Book.objects.all()
for book in all_books: print(book.title)
