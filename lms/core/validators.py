from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

validate_phone_number = RegexValidator(
    r"^\d{10}$",
    _("Неправильный номер телефона."),
    "invalid",
)

validate_identification_number = RegexValidator(
    r"^\d{12}$",
    _("Неправильный идентификационный номер."),
    "invalid",
)
