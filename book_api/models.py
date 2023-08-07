from django.db import models

# Create your models here.
# title, number_of_pages quantity publication_date*/


class Book(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField(default = False)
    publish_date  =models.DateField()
    quantity = models.IntegerField(default = False)
  
    def __str__(self):
        return self.title


# /books/list/
