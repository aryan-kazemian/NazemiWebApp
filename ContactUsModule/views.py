from django.shortcuts import render
from HomeModule import models

# Create your views here.


def contact_us(request):
    current_site_setting = models.SiteSettingsModel.objects.filter(is_active=True).first()
    context = {
        "site_setting": current_site_setting,
    }
    return render(request, 'ContactUs/ContactUs.html', context)