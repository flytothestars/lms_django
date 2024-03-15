from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from velait.velait_django.main.models import BaseModel

from core.validators import validate_identification_number, validate_phone_number
from directory.models import (
    Activity,
    AutomationSystem,
    ParticipationPurpose,
    ProblemOrTask,
)
from courses.models import Course
from listener.models import Listener


class Enrollee(BaseModel):
    listener = models.ForeignKey(
        Listener,
        on_delete=models.CASCADE,
        related_name="enrollees",
        related_query_name="enrollee",
        verbose_name=_("слушатель"),
        null=True,
        blank=True,
    )
    # course_schedule = models.ForeignKey(
    #     "courses.CourseSchedule",
    #     on_delete=models.CASCADE,
    #     related_name="enrollees",
    #     related_query_name="enrollee",
    #     verbose_name=_("расписание курса"),
    #     null=True,
    #     blank=True,
    # )
    link = models.URLField(_("Ссылка на изменение"), null=True, blank=True)
    comment = models.TextField(_("Комментарий"), null=True, blank=True)

    class Meta:
        db_table = "enrollees_enrollee"
        ordering = ["-created_at"]
        verbose_name = _("Абитуриент")
        verbose_name_plural = _("Абитуриенты")

    def __str__(self):
        return self.listener.user.first_name


class TempEnrollee(BaseModel):
    class Lang(models.TextChoices):
        KK = "KK", _("Қазақ тілі")
        RU = "RU", _("Русский язык")

    STATUS_PENDING = "PENDING"
    STATUS_ACCEPTED = "ACCEPTED"
    STATUS_REJECTED = "REJECTED"
    STATUS = Choices(
        (STATUS_PENDING, _("Ожидает рассмотрения")),
        (STATUS_ACCEPTED, _("Одобрено")),
        (STATUS_REJECTED, _("Недействительная анкета")),
    )
    # course_schedule = models.ForeignKey(
    #     "courses.CourseSchedule",
    #     on_delete=models.CASCADE,
    #     related_name="temp_enrollees",
    #     related_query_name="temp_enrollees",
    #     verbose_name=_("расписание курса"),
    #     null=True,
    #     blank=True,
    # )
    link = models.URLField(_("Ссылка на изменение"), null=True, blank=True)
    full_name = models.CharField(_("ФИО Участника (полностью)"), max_length=500)
    phone_number = models.CharField(
        _("Номер телефона с WhatsApp"),
        max_length=10,
        validators=[validate_phone_number],
        help_text=_(
            "без +7, например: 7071231212."
        ),
    )
    
    status = models.CharField(
        _("Статус"),
        choices=STATUS,
        default=STATUS_PENDING,
        max_length=50,
    )
    email = models.CharField(_("Электронный адрес Участника"), max_length=250)
    company_name = models.CharField(_("наименование компании"), max_length=250)
    identification_number = models.CharField(
        _("ИИН/БИН компании"),
        max_length=12,
        validators=[validate_identification_number],
        default="",
    )
    activity = models.ForeignKey(
        Activity,
        verbose_name=_("смотреть стр. СФЕРА_ДЕЯТЕЛЬНОСТИ"),
        on_delete=models.SET_NULL,
        related_name="temp_enrollees",
        related_query_name="temp_enrollee",
        null=True,
        blank=True,
    )
    description = models.TextField(_("Опишите, чем именно занимается Ваша компания"))
    number_of_completed_years = models.DecimalField(
        _("Количество полных лет работы компания"),
        default=0,
        max_digits=10,
        decimal_places=2,
    )
    employee_count = models.PositiveIntegerField(_("количество сотрудников"), default=0)
    is_recording_customers = models.CharField(
        _("Укажите среднемесячное количество клиентов Вашей компании"), default=False, max_length=500
    )
    is_recording_average_check = models.CharField(
        _("Укажите сумму среднемесячного чека в вашей компании"), default=False, max_length=500
    )
    # is_used_automation = models.BooleanField(
    #     _("Применяете ли Вы автоматизацию в своей деятельности"), default=False
    # )
    automation_system = models.ForeignKey(
        AutomationSystem,
        verbose_name=_("Используете ли Вы системы автоматизации в своем бизнесе?"),
        on_delete=models.SET_NULL,
        related_name="temp_enrollees",
        related_query_name="temp_enrollee",
        blank=True,
        null=True,
    )

    course_type = models.ForeignKey(
        Course,
        verbose_name=_("Какие курсы Вы выбираете для обучения?"),
        on_delete=models.SET_NULL,
        related_name="temp_enrollees",
        related_query_name="temp_enrollee",
        blank=True,
        null=True,
    )
    
    # another_automation_system = models.CharField(
    #     _("Какие системы автоматизации Вы используете в компании"), max_length=300, blank=True, null=True
    # )
    problem_or_task = models.ForeignKey(
        ProblemOrTask,
        verbose_name=_(
            "Определите проблемы или задачи бизнеса, которые Вы хотели бы решить в рамках программы обучения"
        ),
        on_delete=models.SET_NULL,
        related_name="temp_enrollees",
        related_query_name="temp_enrollee",
        null=True,
        blank=True,
    )
    # another_problem_or_task = models.CharField(
    #     _("другая проблема или задача"), max_length=300, blank=True, null=True
    # )
    participation_purpose = models.ForeignKey(
        ParticipationPurpose,
        verbose_name=_(
            "Ожидаемые результаты от участия в Программе «Almaty Business 2023»"
        ),
        on_delete=models.SET_NULL,
        related_name="temp_enrollees",
        related_query_name="temp_enrollee",
        null=True,
        blank=True,
    )
    # another_participation_purpose = models.CharField(
    #     _("Ожидаемые результаты от участия в Программе «Almaty Business 2023»"),
    #     max_length=300,
    #     blank=True,
    #     null=True,
    # )
    lang = models.CharField(
        _("Язык обучения"),
        choices=Lang.choices,
        default=Lang.RU,
        max_length=50,
    )
    promo_code = models.CharField(_("промокод"), max_length=250, null=True, blank=True)
    is_complete_course = models.BooleanField(_("курс пройден"), default=False)
    is_emailed = models.BooleanField(_("сообщение отправлено"), default=False)
    email_is_not_valid = models.BooleanField(_("Некорректный email"), default=False)

    class Meta:
        db_table = "enrollees_temp_enrollee"
        ordering = ["-created_at"]
        verbose_name = _("Временный абитуриент")
        verbose_name_plural = _("Временные абитуриенты")

    def __str__(self):
        return self.full_name
