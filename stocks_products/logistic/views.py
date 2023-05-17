from rest_framework import filters

import django_filters
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filterset_fields = ['products']
    filter_backends = [SearchFilter]
    search_fields = ['products__title']

class StockProductTitleFilter(filters.BaseFilterBackend):#ручной фильтр для поиска
    def filter_queryset(self, request, queryset):
        title = request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(products__title=title)
        return queryset