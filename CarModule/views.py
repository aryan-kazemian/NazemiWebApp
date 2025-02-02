from django.shortcuts import render
from django.views.generic import ListView
from . import models
from HomeModule.models import SiteSettingsModel


# Create your views here.

class CarListView(ListView):
     models = models.CarModel
     template_name = 'Car/CarList.html'
     context_object_name = 'cars'

     def get_queryset(self):
         return models.CarModel.objects.filter(is_active=True).all()

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['site_settings'] = SiteSettingsModel.objects.filter(is_active=True).first()
         return context



