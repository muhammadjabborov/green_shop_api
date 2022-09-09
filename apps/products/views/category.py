from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.products.models import Category
from apps.products.serializers.category import CreateProductCategoryModelSerialzier, ProductCategoryModelSerializer
from apps.shared.rest_framework.pagination import CategoryPagination


class ProductCategoryAPIView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductCategoryModelSerializer
    # pagination_class = CategoryPagination
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        """
        DTO
        """
        serializer = CreateProductCategoryModelSerialzier(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        """
        GETa
        """
        categories = self.queryset.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data)
