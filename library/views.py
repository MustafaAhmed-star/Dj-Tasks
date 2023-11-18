from django.shortcuts import render,redirect
from .models import *
from django.views.generic import CreateView, ListView, DetailView,UpdateView, DeleteView

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'
    
class BookCreateView(CreateView):
    model = Book
    template_name = 'library/book_create.html'
    fields = ['title', 'author', 'price']


def book_delete(request, pk):
    book = Book.objects.get(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('library:book-list')

    return render(request, 'library/book_confirm_delete.html', {'book': book})
    
