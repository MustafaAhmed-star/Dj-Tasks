 
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Siebel.views import addComment
from Siebel.api import   PostDetailViewApi
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/<int:pk>', addComment),
    path('posts/<int:pk>/add_comment', addComment),

     
    path('api/posts/<int:pk>/', PostDetailViewApi.as_view() ),
    
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)