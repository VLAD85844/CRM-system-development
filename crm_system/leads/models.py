from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('contacted', 'Контакт установлен'),
        ('converted', 'Конвертирован в клиента'),
        ('lost', 'Потерян')
    ]

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email", blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name="Статус"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Интересующий продукт"
    )
    advertisement = models.ForeignKey(
        'ads.Advertisement',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Рекламная кампания"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='leads',
        verbose_name="Кем создан"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Лид"
        verbose_name_plural = "Лиды"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.get_status_display()})"