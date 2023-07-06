from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings 

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    cover = models.ImageField(upload_to='books/covers', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])

    def __str__(self):
        return self.title
