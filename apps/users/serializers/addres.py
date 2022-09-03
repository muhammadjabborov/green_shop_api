from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.fields import HiddenField
from rest_framework.serializers import ModelSerializer

from apps.users.models import UserAddress


class AddresModelSerializer(ModelSerializer):

    def validate_number(self, number):
        if UserAddress.objects.filter(number=number).exists():
            raise ValidationError("This number already taken")

        if not number:
            raise ValidationError("The number should be in your form_data")

        # if number.isalnum:
        #     raise ValidationError("The number should be only digits")

        return number

    class Meta:
        model = UserAddress
        exclude = ('is_deleted', 'deleted_at')
