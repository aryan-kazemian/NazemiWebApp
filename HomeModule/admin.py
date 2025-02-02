from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.SiteSettingsModel)

admin.site.register(models.QuickLinkModel)

admin.site.register(models.SliderModel)