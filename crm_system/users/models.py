from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('admin', 'Administrator'),
        ('operator', 'Operator'),
        ('marketer', 'Marketer'),
        ('manager', 'Manager'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='operator')

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='user',
    )

    def get_role_display(self):
        return dict(self.ROLES).get(self.role, self.role)