from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.validators import validate_phone_number


class User(AbstractUser):
    patronymic = models.CharField(_("отчество"), max_length=250, blank=True)
    phone_number = models.CharField(
        _("номер телефона"),
        max_length=10,
        blank=True,
        validators=[validate_phone_number],
    )

    def get_full_name(self):
        full_name = f"{self.username} {self.last_name} {self.first_name}"
        return full_name.strip()
