import django_filters
from django.db.models import Count
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.products.filters import ProducrPriceFilter
from apps.shared.rest_framework.pagination import ProductPagination
from apps.products.models import Product, ProductImage, Category
from apps.products.serializers.product import ListProductModelSerializer, ProductImageModelSerializer, \
    ProductModelSerializer, RetrieveProductModelSerializer, CreateProductModelSerializer, UpdateProductModelSerializer


class ProductModelViewSet(ModelViewSet):
    """
      DTO
    """
    queryset = Product.objects.order_by('-created_at')
    serializer_class = ProductModelSerializer
    # permission_classes = (IsAuthenticated,)
    # pagination_class = ProductPagination
    parser_classes = (MultiPartParser,)
    search_fields = ['id', 'title', 'tag']
    lookup_url_kwarg = 'id'
    filterset_fields = {
        'price': ['gte', 'lte']
    }
    filter_backends = [DjangoFilterBackend, SearchFilter]

    @action(detail=False, url_path='product-count', url_name='product-count')
    def get_product_count_by_category(self, request, pk=None, *args, **kwargs):
        """
        THIS IS FOR KNOW CATEGORY-COUNT IN PRODUCTS
        """
        data = Category.objects.annotate(product_count=Count('product_category')).values_list('name', 'product_count')
        return Response(dict(data))

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListProductModelSerializer,
            'create': CreateProductModelSerializer,
            'retrieve': RetrieveProductModelSerializer,
            'put': UpdateProductModelSerializer

        }
        return serializer_dict.get(self.action, ProductModelSerializer)


class ProductImageModelViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    # permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    serializer_class = ProductImageModelSerializer
    # pagination_class = ProductPagination
    lookup_url_kwarg = 'id'
