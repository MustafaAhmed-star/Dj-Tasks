 
from django.contrib import admin
from django.urls import path
from Siebel.views import addComment
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/<int:pk>', addComment),
    path('posts/<int:pk>/add_comment', addComment),
]
