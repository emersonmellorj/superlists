from django.db import models

# Create your models here.
class Item(models.Model):
    
    text = models.TextField(default='', max_length=200)