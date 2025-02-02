from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView
from HomeModule.models import SiteSettingsModel

# Create your views here.

class TutorialListView(ListView):
    model = models.TutorialModel
    template_name = 'Tutorial/TutorialList.html'
    context_object_name = 'tutorials'
    paginate_by = 10

    def get_queryset(self):
        return models.TutorialModel.objects.filter(is_active=True).all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettingsModel.objects.filter(is_active=True).first()
        return context

class TutorialDetailView(DetailView):
    model = models.TutorialModel
    template_name = "Tutorial/TutorialDetail.html"
    context_object_name = 'tutorial'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
