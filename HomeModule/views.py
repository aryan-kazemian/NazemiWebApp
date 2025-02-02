from django.shortcuts import render
from . import models
from CarModule.models import CarModel
from TutorialModule.models import TutorialModel
from ProductModule.models import ProductModel

# Create your views here.

def index(request):
    current_site_setting = models.SiteSettingsModel.objects.filter(is_active=True).first()
    sliders = models.SliderModel.objects.filter(is_active=True).all()
    cars = CarModel.objects.filter(is_active=True, show_on_main=True).all()
    tutorials = TutorialModel.objects.filter(is_active=True, show_on_main=True).all()
    products = ProductModel.objects.filter(is_active=True, show_on_main_page=True).all()

    context = {
        'site_setting': current_site_setting,
        'sliders': sliders,
        'cars': cars,
        'tutorials': tutorials,
        'products': products,
    }
    return render(request, 'Home/Index.html', context)

def header_render_partial_component(request):
    current_site_setting = models.SiteSettingsModel.objects.filter(is_active=True).first()
    context = {
        'site_setting': current_site_setting,
    }
    return render(request, 'Base/Includes/Header.html', context)

def footer_render_partial_component(request):
    current_site_setting = models.SiteSettingsModel.objects.filter(is_active=True).first()
    quick_links = models.QuickLinkModel.objects.filter(is_active=True).all()
    context = {
        'site_setting': current_site_setting,
        'quick_links': quick_links,
    }
    return render(request, 'Base/Includes/Footer.html', context)
