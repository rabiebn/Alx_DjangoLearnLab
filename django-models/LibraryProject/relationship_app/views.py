from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import DetailView

from .models import Library, Book

def get_all_books(request):
    """
    Function-based View that lists all books stored in the DB.
    """
    books = Book.objects.all()
    template = loader.get_template("relationship_app/list_books.html")
    context = {"books": books}
    #output = "\n".join([f"{book.title} - {book.author.name}" for book in books])

    return render(request, "relationship_app/list_books.html", context)

class LibDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    slug_field = 'name'
    slug_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# You need to write a class-based View:
## Read documentations
## You haven't commited anything yet!
##  

