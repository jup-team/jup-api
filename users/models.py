from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    TYPE = (
        ('EMPLOYER', 'Perfil empresa'),
        ('USER', 'Perfil usuário'),
    )
    type_user = models.CharField(max_length=8, choices=TYPE, default='USER')
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return f'User: {self.id}'
