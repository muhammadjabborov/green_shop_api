from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.products.views.category import ProductCategoryAPIView
from app.products.views.product import ProductModelViewSet, ProductImageModelViewSet

router = DefaultRouter()

router.register('product', ProductModelViewSet),
router.register('product-image', ProductImageModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product-category/', ProductCategoryAPIView.as_view(), name='product-category')
]
