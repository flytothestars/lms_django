from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ListenerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "listener"

    verbose_name = _("Слушатели")
