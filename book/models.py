from django.db import models

# Create your models here.

class bookstoremodel(models.Model):
    catagory = (
        ('Histry', 'Histry'),
        ('Science', 'Science'),
        ('Thenology', 'Thenology'),
        ('Lifestyle', 'Lifestyle'),
    )
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    ISBN = models.IntegerField(primary_key=True)
    publication_date = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=20, choices= catagory)
    available_book = models.IntegerField(default=10)
    availability_status = models.BooleanField(default=True)
    
    
    

