from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EnrolleesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "enrollees"
    verbose_name = _("Абитуриенты")

    def ready(self):
        import enrollees.signals  # noqa
