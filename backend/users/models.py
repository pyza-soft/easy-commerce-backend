from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    phone = models.CharField(
        _('phone number'),
        max_length=18,
        null=True,
        blank=True,
        validators=[RegexValidator(r'^\+?(\d*\-)*\d*$')],
    )
