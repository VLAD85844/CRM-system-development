import os
from django.db import models
from django.core.validators import MinValueValidator
from customers.models import Customer
from products.models import Product
from users.models import User

def contract_file_path(instance, filename):
    return f'contracts/{instance.customer.id}/{filename}'

class Contract(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название контракта")
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        verbose_name="Клиент",
        related_name='customer_contracts',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="Услуга",
        related_name='product_contracts',
    )
    document = models.FileField(
        upload_to=contract_file_path,
        verbose_name="Файл договора",
        blank=True,
        null=True,
    )
    signing_date = models.DateField(verbose_name="Дата подписания")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Сумма",
    )
    manager = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Менеджер",
        related_name='manager_contracts',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"
        ordering = ['-signing_date']
        permissions = [
            ('can_manage_contracts', 'Может управлять контрактами'),
        ]

    def __str__(self):
        return f"{self.name} ({self.customer})"

    def filename(self):
        return os.path.basename(self.document.name) if self.document else None

    @property
    def duration(self):
        return f"{(self.end_date - self.start_date).days} дней"