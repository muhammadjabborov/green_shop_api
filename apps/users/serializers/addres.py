from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.fields import HiddenField
from rest_framework.serializers import ModelSerializer

from apps.users.models import UserAddress


class AddresModelSerializer(ModelSerializer):
    class Meta:
        model = UserAddress
        exclude = ('is_deleted', 'deleted_at')
