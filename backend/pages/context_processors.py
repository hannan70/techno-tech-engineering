from site_settings.models import SiteSettings

def get_site_settings(request):
    site_settings = SiteSettings.objects.first()
    return {
        "site_settings": site_settings
    }