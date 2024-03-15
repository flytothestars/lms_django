from django.db import models
from django.utils.translation import gettext_lazy as _
from velait.velait_django.main.models import BaseModel
from ckeditor.fields import RichTextField
from users.models import User
from django.core.exceptions import ValidationError

def validate_image_size(value):
    max_size = 2.5 * 1024 * 1024  # 2.5 мегабайта в байтах
    if value.size > max_size:
        raise ValidationError("Размер изображения не должен превышать 2,5 мегабайта.")

class Teacher(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name="teacher"
    )
    bio = RichTextField(_("Биография"), null=True, blank=True)
    photo = models.ImageField(upload_to="teacher_photos", null=True, blank=True, validators=[validate_image_size])
    experience = models.TextField(_("опыт в бизнесе"), null=True, blank=True)
    link = models.URLField(_("ссылка на видео"), null=True, blank=True)

    class Meta:
        db_table = "teachers_teacher"
        ordering = ["-created_at"]
        verbose_name = _("Тренер")
        verbose_name_plural = _("Тренеры")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    # def __str__(self):
    #     return self.get_photo_url()self.photo.url
