from django.views import generic
from django.urls import reverse_lazy
from .models import Book


# Create your views here.

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'description', 'author', 'price', 'cover']
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'description', 'author', 'price', 'cover']
    template_name = 'books/book_update.html'

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book-list')

