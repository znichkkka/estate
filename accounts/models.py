from django.conf import settings
from django.db import models


class Profile(models.Model):
    SEEKER = 'seeker'
    OWNER = 'owner'
    ROLE_CHOICES = [(SEEKER, 'Соискатель'), (OWNER,'Владелец')]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Пользователь',

    )
    role = models.CharField('Роль', max_length=50, choices=ROLE_CHOICES)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self) -> str:
        return self.user.username
