from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.products.models import Category
from apps.products.serializers.category import CreateProductCategoryModelSerialzier, ProductCategoryModelSerializer


class ProductCategoryAPIView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductCategoryModelSerializer
    # pagination_class = CategoryPagination
    parser_classes = (MultiPartParser,)
    lookup_url_kwarg = 'id'

    def post(self, request, format=None):
        """
        DTO - CREATE VCATEGORY HERE
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = ProductCategoryModelSerializer(category, many=True)
        return Response(serializer.data)
