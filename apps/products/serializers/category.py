from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, HiddenField
from rest_framework.serializers import ModelSerializer

from apps.products.models import Category


class ProductCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CreateProductCategoryModelSerialzier(ModelSerializer):

    def validated_title(self, title):
        if Category.objects.filter(title=title).exists():
            raise ValidationError('This category name already exists')
        return title

    class Meta:
        model = Category
        fields = ('id', 'name')
