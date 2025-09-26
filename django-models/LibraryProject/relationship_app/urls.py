from django.urls import path

from . import views

urlpatterns = [
    path('all_books/', views.get_all_books, name='books_all'),
    path('all_books/<int:pk>', views.LibDetailView.as_view(), name='library_books')
]