from django.urls import path
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    path('all_books/', list_books(), name='books_all'),
    path('all_books/<int:pk>', LibraryDetailView.as_view(), name='library_books')
]