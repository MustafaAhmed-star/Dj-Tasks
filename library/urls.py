from django.urls import path
from .views import BookListView,BookDetailView,BookCreateView,book_delete
app_name = 'library'
urlpatterns = [
   path('books/', BookListView.as_view(),name = 'book-list'),
   path('books/<int:pk>/', BookDetailView.as_view()),
   path('books/create/', BookCreateView.as_view()),
   path('books/<int:pk>/delete/', book_delete ), 


]
