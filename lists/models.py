from django.db import models
from django.urls import reverse

# Create your models here.
class List(models.Model):
    
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

    pass

class Item(models.Model):
    
    text = models.TextField(default='', max_length=200)
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
    