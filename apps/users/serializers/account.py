from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import ModelSerializer

from apps.users.models import UserImage


class ChangeAccountModelSerializer(ModelSerializer):
    first_name = CharField(max_length=255, required=False)
    last_name = CharField(max_length=255, required=False)
    email = EmailField(max_length=255, required=False)
    number = CharField(required=False)

    # username = CharField(max_length=255,required=False)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email already exists")
        return email

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username already exists")
        return username

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'number')


class ChangeAccountAvatarModelSerializer(ModelSerializer):
    class Meta:
        model = UserImage
        fields = ('id', 'user_id', 'image')


class AvatarModelSerializer(ModelSerializer):

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['images'] = ChangeAccountAvatarModelSerializer(instance.product_image.first()).data
        return represent

    class Meta:
        model = User
        fields = '__all__'
