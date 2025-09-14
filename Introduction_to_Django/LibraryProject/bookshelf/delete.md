from bookshelf.models import Book

book_to_delete = Book.objects.get(title='1984')
book_to_delete.delete()