from django.db import models
from django.utils.translation import gettext_lazy as _
from velait.velait_django.main.models import BaseModel


class ActivityCategory(BaseModel):
    name = models.CharField(_("название"), max_length=250)

    class Meta:
        db_table = "directory_activity_category"
        ordering = ["name"]
        verbose_name = _("категория сферы деятельности")
        verbose_name_plural = _("категории сферы деятельности")

    def __str__(self):
        return self.name


class Activity(BaseModel):
    name = models.CharField(_("название"), max_length=250)
    activity_category = models.ForeignKey(
        ActivityCategory,
        verbose_name=_("категория сферы деятельности"),
        on_delete=models.SET_NULL,
        related_name="activities",
        related_query_name="activity",
        null=True,
    )

    class Meta:
        db_table = "directory_activity"
        ordering = ["name"]
        verbose_name = _("сфера деятельности")
        verbose_name_plural = _("сферы деятельности")

    def __str__(self):
        return self.name


class AutomationSystem(BaseModel):
    name = models.CharField(_("название"), max_length=250)
    is_other = models.BooleanField(_("другое"), default=False)

    class Meta:
        db_table = "directory_automation_system"
        ordering = ["name"]
        verbose_name = _("система автоматизации")
        verbose_name_plural = _("системы автоматизации")

    def __str__(self):
        return self.name


class ProblemOrTask(BaseModel):
    name = models.CharField(_("название"), max_length=300)
    is_other = models.BooleanField(_("другое"), default=False)

    class Meta:
        db_table = "directory_problem_or_task"
        ordering = ["name"]
        verbose_name = _("проблема или задача")
        verbose_name_plural = _("проблемы или задачи")

    def __str__(self):
        return self.name


class ParticipationPurpose(BaseModel):
    name = models.CharField(_("название"), max_length=300)
    is_other = models.BooleanField(_("другое"), default=False)

    class Meta:
        db_table = "directory_participation_purpose"
        ordering = ["name"]
        verbose_name = _("цель участия")
        verbose_name_plural = _("цели участия")

    def __str__(self):
        return self.name
