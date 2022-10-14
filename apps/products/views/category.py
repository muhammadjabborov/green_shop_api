from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet

from apps.products.models import Category
from apps.products.serializers.category import CreateProductCategoryModelSerialzier, ProductCategoryModelSerializer


class ProductCategoryAPIView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateProductCategoryModelSerialzier
    # pagination_class = CategoryPagination
    lookup_url_kwarg = 'id'
    permission_classes = AllowAny

    def get_permissions(self):
        if self.request.method == "POST":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def post(self, request, format=None):
        """
        DTO - CREATE CATEGORY HERE
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

