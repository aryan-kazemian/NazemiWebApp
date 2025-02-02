from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',  views.admin_panel, name='admin_panel'),
]