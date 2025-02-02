from django.urls import path
from . import views

urlpatterns = [
    path("", views.TutorialListView.as_view(), name="TutorialListPage"),
    path('<slug:slug>/', views.TutorialDetailView.as_view(), name='TutorialDetailPage'),

]