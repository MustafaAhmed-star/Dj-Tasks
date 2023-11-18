from django.urls import path
from .views import BookListView,BookDetailView,BookCreateView
urlpatterns = [
   path('books/', BookListView.as_view()),
   path('books/<int:pk>/', BookDetailView.as_view()),
   path('books/create/', BookCreateView.as_view(), name='book-create'),

]
