from django.db import models
from django.utils.translation import gettext_lazy as _
from velait.velait_django.main.models import BaseModel

from teachers.models import Teacher


class CourseSpecification(BaseModel):
    name = models.CharField(_("название"), max_length=500, null=True, blank=True)
    description = models.TextField(_("описание"), null=True, blank=True)
    photo = models.ImageField(_("фото"), upload_to="static/img/media/course_photo", null=True, blank=True)

    class Meta:
        db_table = "courses_course_specification"
        ordering = ["-created_at"]
        verbose_name = _("спецификация курса")
        verbose_name_plural = _("спецификация курса")

    def __str__(self):
        return self.name


class Course(BaseModel):
    name = models.CharField(_("название курса"), max_length=500, null=True, blank=True)
    description = models.TextField(_("описание курса"), null=True, blank=True)
    start_date = models.DateTimeField(_("дата начала"), null=True, blank=True)
    end_date = models.DateTimeField(_("дата завершения"), null=True, blank=True)
    course_assessment_link = models.URLField(
        _("ссылка на оценку курса"), null=True, blank=True
    )
    knowledge_assessment_link = models.URLField(
        _("ссылка на оценку знаний"), null=True, blank=True
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="courses",
        related_query_name="course",
        verbose_name=_("тренер"),
        null=True,
        blank=True,
    )
    course_specification = models.ForeignKey(
        CourseSpecification,
        on_delete=models.CASCADE,
        related_name="courses",
        related_query_name="course",
        verbose_name=_("спецификация курса"),
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "courses_course"
        ordering = ["-created_at"]
        verbose_name = _("Курс")
        verbose_name_plural = _("Курсы")

    def __str__(self):
        return self.name


class CourseSchedule(BaseModel):
    course = models.ForeignKey(
        Course,
        verbose_name=_("курс"),
        related_name="course_schedules",
        related_query_name="course_schedule",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    teacher = models.ForeignKey(
        Teacher,
        verbose_name=_("тренер"),
        related_name="course_schedules",
        related_query_name="course_schedule",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    start_date = models.DateField(_("дата начала"), null=True, blank=True)
    end_date = models.DateField(_("дата завершения"), null=True, blank=True)
    start_time = models.TimeField(_("время начала"), null=True, blank=True)
    end_time = models.TimeField(_("время завершения"), null=True, blank=True)
    is_complete = models.BooleanField(_("курс завершен"), default=False)

    class Meta:
        db_table = "courses_course_schedule"
        ordering = ["created_at"]
        verbose_name = _("расписание курса")
        verbose_name_plural = _("расписания курсов")

    def __str__(self):
        return f"{self.course.name} {self.teacher.user} {self.start_date}"


class CourseSession(BaseModel):
    # temp_enrollee = models.ManyToManyField(
    #     TempEnrollee,
    #     through="CourseSessionListener",
    #     through_fields=("course_session", "listener"),
    #     related_name="course_sessions",
    #     related_query_name="course_session",
    #     verbose_name=_("абитуриенты"),
    # )
    course_schedule = models.ForeignKey(
        CourseSchedule,
        on_delete=models.CASCADE,
        related_name="course_sessions",
        related_query_name="course_session",
        verbose_name=_("расписание курса"),
    )

    class Meta:
        db_table = "courses_course_session"
        ordering = ["-created_at"]
        verbose_name = _("Группа абитуриентов")
        verbose_name_plural = _("Группы абитуриентов")


class CourseSessionListener(BaseModel):
    course_session = models.ForeignKey(CourseSession, on_delete=models.CASCADE)
    # listener = models.ForeignKey(TempEnrollee, on_delete=models.CASCADE)

    class Meta:
        db_table = "courses_course_session_listener"
        ordering = ["created_at"]
        verbose_name = _("абитуриент группы")
        verbose_name_plural = _("абитуриенты группы")

    def __str__(self):
        return f"{self.listener}"


class Lesson(BaseModel):
    name = models.CharField(_("название"), max_length=500, null=True, blank=True)
    description = models.TextField(_("описание"), null=True, blank=True)
    course = models.ForeignKey(
        Course,
        verbose_name=_("курс"),
        on_delete=models.CASCADE,
        related_name="lessons",
        related_query_name="lesson",
    )

    class Meta:
        db_table = "courses_lesson"
        ordering = ["created_at"]
        verbose_name = _("занятие")
        verbose_name_plural = _("занятия")

    def __str__(self):
        return self.name


class VideoCourseCategory(BaseModel):
    name = models.CharField(_("название"), max_length=500, null=True, blank=True)
    description = models.TextField(_("описание"), null=True, blank=True)

    class Meta:
        db_table = "courses_video_course_category"
        ordering = ["created_at"]
        verbose_name = _("категория видео курса")
        verbose_name_plural = _("категории видео курсов")

    def __str__(self):
        return self.name


class VideoCourse(BaseModel):
    name = models.CharField(_("название"), max_length=500, null=True, blank=True)
    description = models.TextField(_("описание"), null=True, blank=True)
    video_course_category = models.ForeignKey(
        VideoCourseCategory,
        verbose_name=_("категория видео курса"),
        on_delete=models.CASCADE,
        related_name="video_courses",
        related_query_name="video_course",
    )
    link = models.URLField(_("ссылка на видео"), null=True, blank=True)

    class Meta:
        db_table = "courses_video_course"
        ordering = ["created_at"]
        verbose_name = _("видео курс")
        verbose_name_plural = _("видео курсы")

    def __str__(self):
        return self.name
