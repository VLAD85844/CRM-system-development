from decimal import Decimal
from django.db import models
from products.models import Product
from django.core.validators import MinValueValidator

class Advertisement(models.Model):
    CHANNEL_CHOICES = [
        ('social', 'Социальные сети'),
        ('search', 'Поисковые системы'),
        ('email', 'Email-рассылка'),
        ('offline', 'Оффлайн-реклама')
    ]

    name = models.CharField(max_length=100, unique=True, verbose_name="Название кампании")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Рекламируемая услуга",
        related_name='advertisements'
    )
    channel = models.CharField(
        max_length=20,
        choices=CHANNEL_CHOICES,
        verbose_name="Канал продвижения"
    )
    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Бюджет (руб)"
    )
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    class Meta:
        verbose_name = "Рекламная кампания"
        verbose_name_plural = "Рекламные кампании"
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.name} ({self.get_channel_display()})"

    @property
    def leads_count(self):
        return self.lead_set.count()

    @property
    def customers_count(self):
        from customers.models import Customer
        return Customer.objects.filter(lead__advertisement=self).count()

    @property
    def profit(self):
        from contracts.models import Contract
        contracts = Contract.objects.filter(product=self.product)
        if contracts.exists() and self.budget > 0:
            total = sum(c.amount for c in contracts)
            return Decimal(total) / Decimal(str(self.budget))
        return None