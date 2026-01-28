from django.shortcuts import render
from banners.models import Banner
from site_settings.models import SiteSettings
from categories.models import Category

# Create your views here.
def home_page(request):
    banner = Banner.objects.order_by("-id").first()
    site_settings = SiteSettings.objects.first()
    categories = Category.objects.all()
    context = {
        "banner": banner, 
        "site_settings": site_settings,
        "categories" : categories
    }
    return render(request, "index.html", context)
