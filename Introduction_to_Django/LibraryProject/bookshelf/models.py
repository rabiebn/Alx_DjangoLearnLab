from django.db import models

class Book(models.Model):
    '''
    Defines Book class
    '''
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    
