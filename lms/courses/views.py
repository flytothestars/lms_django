from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView

from core.mixins import BasePageMixin
from courses.models import Course, VideoCourse, VideoCourseCategory


class CourseList(BasePageMixin, ListView):
    title = _("Курсы")
    model = Course
    template_name = "courses/courses_list.html"
    nav_section = "courses"
    nav_tab = "course"


class VideoCourseList(BasePageMixin, ListView):
    title = _("Видеоуроки")
    model = VideoCourse
    template_name = "courses/video_courses.html"
    nav_section = "courses"
    nav_tab = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        video_course_categories = VideoCourseCategory.objects.all()
        context["video_course_categories"] = video_course_categories
        return context
