from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="ProductListPage"),
    re_path(r'^(?P<slug>[\w\u0600-\u06FF-]+)/$', views.ProductDetailView.as_view(), name='ProductDetailPage'),
    path('api/search/', views.SearchItemsView.as_view(), name='SearchItemAPI'),
]
