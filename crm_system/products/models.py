from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость', default=0)

    def __str__(self):
        return self.name