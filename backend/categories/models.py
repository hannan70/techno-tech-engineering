from django.db import models
from PIL import Image

# def category_image_size(image):
#     img = Image.open(image)
#     width, height = img.size
    
    # REQUIRED_WIDTH =
    # REQUIRED_HEIGHT = 


# Create your models here.
class Category(models.Model):
    image         = models.ImageField(upload_to="photos")
    category_name = models.CharField(max_length=255, unique=True)
    qty           = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['category_name']
    
    
    def __str__(self):
        return self.category_name