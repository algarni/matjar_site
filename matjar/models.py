from django.db import models
from django.utils.timezone import now
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


# Create your models here.
class Category(models.Model):
    name = models.CharField('اسم الصنف', max_length=50)

    def __str__(self):
        return "Category ID: {}".format(self.id)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=False)
    show_on_homepage = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "Product# {}".format(self.id)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images')
    image_title = models.CharField(max_length=100)
    image_description = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    thumbnail = ImageSpecField(source=image,
                               processors=[ResizeToFit(100, 100)],
                               format='JPEG',
                               options={'quality': 60})

    medium = ImageSpecField(source=image,
                            processors=[ResizeToFit(320, 150)],
                            format='JPEG',
                            options={'quality': 60})

    large = ImageSpecField(source=image,
                           processors=[ResizeToFit(580, 420)],
                           format='JPEG',
                           options={'quality': 60})


class Order(models.Model):
    created = models.DateTimeField(default=now, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
    )
    anonymous_user_email = models.EmailField(
        blank=True,
        default='',
        editable=False,
    )
    items = models.ManyToManyField(Product, through='OrderItem')


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
