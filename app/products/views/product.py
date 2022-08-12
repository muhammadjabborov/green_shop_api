from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from app.shared.rest_framework.pagination import ProductPagination
from app.products.models import Product, ProductImage, Category
from app.products.serializers.product import ListProductModelSerializer, ProductImageModelSerializer, \
    ProductModelSerializer, RetrieveProductModelSerializer, CreateProductModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = ProductPagination
    lookup_url_kwarg = 'id'

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListProductModelSerializer,
            'create': CreateProductModelSerializer,
            'retrieve': RetrieveProductModelSerializer,

        }
        return serializer_dict.get(self.action, ProductModelSerializer)

    @action(detail=False, url_path='product-count', url_name='product-count')
    def get_product_count_by_category(self, request, pk=None, *args, **kwargs):
        data = Category.objects.annotate(product_count=Count('product')).values_list('name', 'product_count')
        return Response(dict(data))


class ProductImageModelViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    serializer_class = ProductImageModelSerializer
    pagination_class = ProductPagination
    lookup_url_kwarg = 'id'
