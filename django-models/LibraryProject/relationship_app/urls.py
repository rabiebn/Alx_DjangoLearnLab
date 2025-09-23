from django.urls import path

from . import views

urlpatterns = [
    path('all_books/', views.get_all_books, name='AllBooks'),
    path('all_books/<str:library_name>', views.LibListView.as_view(), name='AllLibBooks')
]