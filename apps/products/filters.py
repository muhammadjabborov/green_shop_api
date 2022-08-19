from django_filters import FilterSet, RangeFilter, NumberFilter

from apps.products.models import Product


class ProducrPriceFilter(FilterSet):
    price = RangeFilter(field_name='price')

    class Meta:
        model = Product
        fields = ['price']
