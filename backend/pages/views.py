from django.shortcuts import render, get_object_or_404
from banners.models import Banner
from site_settings.models import SiteSettings
from categories.models import Category
from brands.models import Brand
from products.models import Product

# Create your views here.
def home_page(request):
    banner = Banner.objects.order_by("-id").first()
    site_settings = SiteSettings.objects.first()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    
    context = {
        "banner": banner, 
        "site_settings": site_settings,
        "categories" : categories,
        "brands": brands,
        "products": products
    }
    return render(request, "index.html", context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }
    return render(request, "inc/product_details.html", context)
