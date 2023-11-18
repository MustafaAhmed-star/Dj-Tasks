from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    biography = models.TextField(max_length=2000)
    
    
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200) 
    author =models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return f'{self.title}:{self.author}'
        