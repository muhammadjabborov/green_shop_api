from django_filters import FilterSet, RangeFilter, NumberFilter

from app.products.models import Product


class ProducrPriceFilter(FilterSet):
    # price = NumberFilter(field_name='price', lookup_expr=)

    class Meta:
        model = Product
        fields = ['price']
