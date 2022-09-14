from django.contrib.gis.geoip2.resources import Country
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.migrations.serializer import ChoicesSerializer
from django.db.models import Model, CharField, IntegerField, FloatField, JSONField, SlugField, ForeignKey, CASCADE, \
    TextField, ImageField, TextChoices, EmailField
from django.utils.text import slugify

from apps.shared.models import BaseModel, DeletedModel


class Category(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name

    @property
    def count_product(self):
        return self.product_category.count()

    class Meta:
        verbose_name_plural = 'Category'
        db_table = 'category'


class Product(BaseModel, DeletedModel):
    class Type(TextChoices):
        SIZE_S = "S"
        SIZE_M = "M"
        SIZE_L = "L"
        SIZE_XL = "XL"

    title = CharField(max_length=255)
    price = FloatField()
    short_description = CharField(max_length=255)
    long_description = TextField()
    rating = IntegerField(
        validators=[
            MaxValueValidator(5, 'Product should have minimal 5 score'),
            MinValueValidator(1, 'Product should have maximal 1 score')
        ]
    )
    size = CharField(max_length=25, choices=Type.choices, default=Type.SIZE_S)
    tag = CharField(max_length=255)
    category = ForeignKey(Category, on_delete=CASCADE, related_name='product_category')

    @property
    def images(self):
        return self.product_image.all()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Product'
        db_table = 'product'


class ProductImage(Model):
    product = ForeignKey(Product, CASCADE, related_name='product_image')
    image = ImageField(upload_to='images/')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name_plural = 'ProductImage'
        db_table = 'product_image'


class JoinUser(Model):
    email = EmailField(max_length=255)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'JoinedUser'
        db_table = 'joined_users'
