from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        verbose_name: 'Пользователя'
        verbose_name_plural: 'Пользователи'

    def __str__(self):
        return self.username

#g-a223
#absd1234