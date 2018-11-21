from django.db import models


class BrandType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Products(models.Model):
    STATUS_IN_STOCK = 0
    STATUS_OUT_STOCK = 1
    STATUS_PENDING = 2
    STATUS_NOT_PENDING = 3
    STATUS_DENY = 4
    STATUS_CHOICES = (
        (STATUS_IN_STOCK, 'В наличии'),
        (STATUS_OUT_STOCK, 'Нет в наличии'),
        (STATUS_PENDING, 'Ожидается'),
        (STATUS_NOT_PENDING, 'Не ожидается'),
        (STATUS_DENY, 'Снято с продаж'),
    )

    name = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=STATUS_IN_STOCK)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    count = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products')
    brand_type = models.ForeignKey(BrandType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    @property
    def price_for_stripe(self):
        return self.price * 100