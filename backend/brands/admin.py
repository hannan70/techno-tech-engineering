from django.contrib import admin
from . models import Brand
from django.utils.html import format_html

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', )
    
    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" style="border-radius:3px;" />',
                obj.image.url
            )
        else:
            return "No Image"
        
    thumbnail.short_description = "Photo"
    


admin.site.register(Brand, BrandAdmin)