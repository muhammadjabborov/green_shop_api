from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from app.products.models import Category
from app.products.serializers.category import CreateProductCategoryModelSerialzier, ProductCategoryModelSerializer
from app.shared.rest_framework.pagination import CategoryPagination


class ProductCategoryAPIView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductCategoryModelSerializer
    # pagination_class = CategoryPagination
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser,)


    def post(self, request, format=None):
        serializer = CreateProductCategoryModelSerialzier(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        categories = self.queryset.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data)

