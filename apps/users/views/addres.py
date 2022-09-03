from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from apps.users.models import UserAddress
from apps.users.serializers.addres import AddresModelSerializer


class AddresModelViewSet(ModelViewSet):
    serializer_class = AddresModelSerializer
    queryset = UserAddress.objects.all()
    parser_classes = (MultiPartParser,)
    lookup_url_kwarg = 'id'

