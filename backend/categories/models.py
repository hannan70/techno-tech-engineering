from django.db import models
from PIL import Image
import os


# Create your models here.
class Category(models.Model):
    image         = models.ImageField(upload_to="category")
    category_name = models.CharField(max_length=255, unique=True)
    qty           = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['category_name']
    
    
    # when i update then image then first delete for old image
    def save(self, *args, **kwargs):
        if self.pk:
            old = Category.objects.get(pk=self.pk)
            if old.image and old.image != self.image:
                if os.path.isfile(old.image.path):
                    os.remove(old.image.path)
        super().save(*args, **kwargs)
    
    
    # delete image
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)
    
    
    def __str__(self):
        return self.category_name