from django.db import models

# Create your models here.
class Category(models.Model):
    image      = models.ImageField(upload_to="photos")