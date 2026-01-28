from django.db import models
import os

# Create your models here.
class Brand(models.Model):
    image = models.ImageField(upload_to="brand")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    # when i update then image then first delete for old image
    def save(self, *args, **kwargs):
        if self.pk:
            old = Brand.objects.get(pk=self.pk)
            if old.image and old.image != self.image:
                if os.path.isfile(old.image.path):
                    os.remove(old.image.path)
        super().save(*args, **kwargs)
    
    # delete image
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)