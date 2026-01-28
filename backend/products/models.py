from django.db import models
import os
from ckeditor.fields import RichTextField
from PIL import Image
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

def validate_image_size(image):
    img = Image.open(image)
    width, height = img.size

    REQUIRED_WIDTH = 1300
    REQUIRED_HEIGHT = 655

    if width != REQUIRED_WIDTH or height != REQUIRED_HEIGHT:
        raise ValidationError(
            f"Image size must be {REQUIRED_WIDTH} x {REQUIRED_HEIGHT} pixels"
        )
        


# Create your models here.
class Product(models.Model):
    product_title = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    image = models.ImageField(upload_to="products/", validators=[validate_image_size])
    brand_name    = models.CharField(max_length=255)
    stock = models.PositiveIntegerField(default=0)
    description =  RichTextField()
    price_logn_description = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # when i update then image then first delete for old image
    def save(self, *args, **kwargs):
        if self.pk:
            old = Product.objects.get(pk=self.pk)
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
        return self.product_title