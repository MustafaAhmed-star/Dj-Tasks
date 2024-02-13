from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null = True, blank = True)
    title = models.CharField(max_length=50,null = True, blank = True)
    content = models.TextField(null = True, blank = True)
    image = models.ImageField(upload_to='post',null = True, blank = True)
    create_at = models.DateTimeField(default=timezone.now,null = True, blank = True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True, blank = True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null = True, blank= True)
    content = models.TextField(max_length=1000)
    create_at = models.DateTimeField(default=timezone.now,null = True, blank = True)
    def __str__(self):
        return f"{self.post}--->{self.user}"