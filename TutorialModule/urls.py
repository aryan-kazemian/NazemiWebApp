from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.TutorialListView.as_view(), name="TutorialListPage"),
    re_path(r'^(?P<slug>[\w\u0600-\u06FF-]+)/$', views.TutorialDetailView.as_view(), name='TutorialDetailPage'),
]
