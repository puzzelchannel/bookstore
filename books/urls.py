from django.urls import path

from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, book_detail

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<int:pk>/book-detail/', book_detail, name='book-detail'),
    path('book-create/', BookCreateView.as_view(), name='book-create'),
    path('<int:pk>/book-update/', BookUpdateView.as_view(), name='book-update'),
    path('<int:pk>/book-delete/', BookDeleteView.as_view(), name='book-delete'),
]
