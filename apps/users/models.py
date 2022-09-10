from django.contrib.auth.models import AbstractUser, PermissionsMixin, User
from django.core.validators import MaxValueValidator, MinValueValidator, integer_validator
from django.db import models
from django.db.models import TextChoices, ForeignKey, CASCADE, ImageField, IntegerField
import os

from apps.shared.models import DeletedModel, BaseModel





class UserImage(BaseModel, DeletedModel):
    user = ForeignKey(User, CASCADE, related_name='user_image')
    image = ImageField(upload_to='user-images/', default='media/images/avatar.png')


class UserAddress(BaseModel, DeletedModel):
    class CountryChoices(TextChoices):
        AF = 'Afghanistan',
        AX = 'Åland Islands',
        AL = 'Albania',
        DZ = 'Algeria',
        AS = 'American Samoa',
        AD = 'AndorrA',
        AO = 'Angola',
        AI = 'Anguilla',
        AQ = 'Antarctica',
        AG = 'Antigua and Barbuda',
        AR = 'Argentina',
        AM = 'Armenia',
        AW = 'Aruba',
        AU = 'Australia',
        AT = 'Austria',
        AZ = 'Azerbaijan',
        BS = 'Bahamas',
        BH = 'Bahrain',
        BD = 'Bangladesh',
        BB = 'Barbados',
        BY = 'Belarus',
        BE = 'Belgium',
        BZ = 'Belize',
        BJ = 'Benin',
        BM = 'Bermuda',
        BT = 'Bhutan',
        BO = 'Bolivia',
        BA = 'Bosnia and Herzegovina',
        BW = 'Botswana',
        BV = 'Bouvet Island',
        BR = 'Brazil',
        IO = 'British Indian Ocean Territory',
        BN = 'Brunei Darussalam',
        BG = 'Bulgaria',
        BF = 'Burkina Faso',
        UZ = 'Uzbekistan'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country_region = models.CharField(max_length=45, choices=CountryChoices.choices, default=CountryChoices.UZ)
    city = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=6)
    # email = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=25)
