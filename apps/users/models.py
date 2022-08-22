from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import TextChoices

from apps.shared.models import DeletedModel, BaseModel


class User(AbstractUser, PermissionsMixin, BaseModel, DeletedModel):
    # is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class UserAddress(BaseModel, DeletedModel):
    class CountryChoices(TextChoices):
        UZB = "UZBEKISTAN"
        RUS = "RUSSIA"
        USA = "USA"

    class CityChoices(TextChoices):
        TAS = "TASHKENT"
        MOS = "MOSCOW"
        VAS = "VASHINGTON"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country_region = models.CharField(max_length=25, choices=CountryChoices.choices, default=CountryChoices.UZB)
    city = models.CharField(max_length=25, choices=CityChoices.choices, default=CityChoices.TAS)
    zip = models.CharField(max_length=6)
    email = models.ForeignKey('users.User', on_delete=models.CASCADE)
    phone_number = models.IntegerField(validators=[
        MaxValueValidator(25, 'The max phone number length is 25'),
        MinValueValidator(5, 'The min phone number length is 5')
    ])
