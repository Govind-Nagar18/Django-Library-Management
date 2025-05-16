from django.urls import path
from .views import BooksView, BooksDetailsView

urlpatterns = [
    path('books/', BooksView.as_view(), name='book-data'),
    path('books/<int:pk>/', BooksDetailsView.as_view(), name='book-details'),
]