from rest_framework.serializers import ModelSerializer

from apps.products.models import Product, ProductImage

# product_image
from apps.products.serializers.category import ProductCategoryModelSerializer


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


# product_model
class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# product_get_queryset
class ListProductModelSerializer(ModelSerializer):

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['images'] = ProductImageModelSerializer(instance.product_image.first()).data
        return represent

    class Meta:
        model = Product
        fields = ('id', 'title', 'price')


# product_detail_get
class RetrieveProductModelSerializer(ModelSerializer):
    images = ProductImageModelSerializer(many=True)
    category = ProductCategoryModelSerializer(read_only=True)

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'deleted_at', 'is_deleted')


# product_create
class CreateProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'deleted_at', 'is_deleted')


class UpdateProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ('deleted_at', 'is_deleted')
