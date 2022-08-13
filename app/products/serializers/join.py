from rest_framework.exceptions import ValidationError
from rest_framework.fields import EmailField
from rest_framework.serializers import ModelSerializer

from app.products.models import JoinUser


class JoinModelSerializer(ModelSerializer):
    email = EmailField(max_length=255)

    def validate_email(self, email):
        if JoinUser.objects.filter(email=email).exists():
            raise ValidationError('This email already exists')

        return email

    class Meta:
        model = JoinUser
        fields = '__all__'

