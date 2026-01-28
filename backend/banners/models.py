from django.db import models
import os
from django.core.exceptions import ValidationError
from PIL import Image

def validate_image_size(image):
    img = Image.open(image)
    width, height = img.size

    REQUIRED_WIDTH = 1920
    REQUIRED_HEIGHT = 1000

    if width != REQUIRED_WIDTH or height != REQUIRED_HEIGHT:
        raise ValidationError(
            f"Image size must be {REQUIRED_WIDTH} x {REQUIRED_HEIGHT} pixels"
        )
        
        

# Create your models here.
class Banner(models.Model):
    title           = models.CharField(max_length=255)
    sub_title       = models.CharField(max_length=255)
    image           = models.ImageField(upload_to="photos", validators=[validate_image_size]) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    # delete for old image
    def save(self, *args, **kwargs):
        if self.pk:
            old = Banner.objects.get(pk=self.pk)
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
        return self.title
    