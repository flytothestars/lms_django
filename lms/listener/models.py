from django.db import models
from django.utils.translation import gettext_lazy as _
from velait.velait_django.main.models import BaseModel

from users.models import User


class Listener(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="listener"
    )

    class Meta:
        db_table = "listeners_listener"
        ordering = ["-created_at"]
        verbose_name = _("Слушатель")
        verbose_name_plural = _("Слушатели")

    def __str__(self):
        return self.user
