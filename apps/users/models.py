from django.contrib.auth.models import AbstractUser, PermissionsMixin, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import TextChoices

from apps.shared.models import DeletedModel, BaseModel




class UserAddress(BaseModel, DeletedModel):
    class CountryChoices(TextChoices):
        UZB = "UZBEKISTAN/TAS"
        RUS = "RUSSIA/MOS"
        USA = "USA/VAS"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country_region = models.CharField(max_length=25, choices=CountryChoices.choices, default=CountryChoices.UZB)
    city = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=6)
    # email = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=25)
