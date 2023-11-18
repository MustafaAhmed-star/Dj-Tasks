from django.shortcuts import render
from .models import Author ,Book ,Review
from django.views.generic import CreateView, ListView, DetailView,UpdateView, DeleteView

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
