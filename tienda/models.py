from django.db import models

# Create your models here.
class Productos(models.Model):
        
    nombre= models.CharField(max_length=30)