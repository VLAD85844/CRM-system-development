from django.db import models
from leads.models import Lead
from users.models import User

class Customer(models.Model):
    lead = models.OneToOneField(
        Lead,
        on_delete=models.PROTECT,
        verbose_name="Источник (лид)"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Ответственный"
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Активный'),
            ('inactive', 'Неактивный'),
            ('premium', 'Премиум')
        ],
        default='active',
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.lead.last_name} {self.lead.first_name}"