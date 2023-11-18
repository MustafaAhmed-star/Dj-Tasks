from django.shortcuts import render
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
