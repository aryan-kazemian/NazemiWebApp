from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView
from HomeModule.models import SiteSettingsModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.

class ProductListView(ListView):
    model = models.ProductModel
    template_name = 'Product/ProductList.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        queryset = models.ProductModel.objects.filter(is_active=True)

        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)

        sort_by = self.request.GET.get('sort_by')
        if sort_by in ['price_integer', '-price_integer', 'id', '-id']:
            queryset = queryset.order_by(sort_by)

        car_slug = self.request.GET.get('car')
        if car_slug:
            queryset = queryset.filter(car__slug=car_slug)

        search_query_1 = self.request.GET.get('q1')
        search_query_2 = self.request.GET.get('q2')

        # Ensure that only one search query is used at a time
        if search_query_1:
            queryset = queryset.filter(name__icontains=search_query_1)
        elif search_query_2:
            queryset = queryset.filter(name__icontains=search_query_2)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.ProductCategoryModel.objects.filter(is_active=True).all()
        context['all_product_quantity'] = models.ProductModel.objects.filter(is_active=True).count()

        sort_by = self.request.GET.get('sort_by')
        if sort_by in ['price_integer', '-price_integer', 'id', '-id']:
            context['sort_by'] = sort_by

        return context



class ProductDetailView(DetailView):
    model = models.ProductModel
    template_name = "Product/ProductDetails.html"
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['site_settings'] = SiteSettingsModel.objects.filter(is_active=True).first()

        return context


class SearchItemsView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            items = models.ProductModel.objects.filter(name__icontains=query)
            serializer = serializers.ItemSerializer(items, many=True)
            return Response(serializer.data)
        return Response([], status=status.HTTP_200_OK)