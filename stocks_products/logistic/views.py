from rest_framework import filters

import django_filters
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
<<<<<<< HEAD
    filterset_fields = ['products', 'products__title']
    # filter_backends = [SearchFilter]
    # search_fields = ['products__title']
=======
    filterset_fields = ['products']
    filter_backends = [SearchFilter]
    search_fields = ['products__title']
>>>>>>> 8db15544313b98612c2c1f0df5c40754f17a6d95

class StockProductTitleFilter(filters.BaseFilterBackend):#ручной фильтр для поиска
    def filter_queryset(self, request, queryset):
        title = request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(products__title=title)
        return queryset