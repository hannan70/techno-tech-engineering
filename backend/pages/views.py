from django.shortcuts import render
from banners.models import Banner
from site_settings.models import SiteSettings

# Create your views here.
def home_page(request):
    banner = Banner.objects.order_by("-id").first()
    site_settings = SiteSettings.objects.first()
    return render(request, "base.html", context={"banner": banner, "site_settings": site_settings})
