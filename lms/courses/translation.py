from modeltranslation.translator import TranslationOptions, register

from courses.models import Course


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ("name", "description")
