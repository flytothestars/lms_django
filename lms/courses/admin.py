from django.contrib import admin
from modeltranslation.admin import TranslationAdmin  # noqa

from courses.models import (
    Course,
    CourseSchedule,
    CourseSession,
    CourseSessionListener,
    CourseSpecification,
    Lesson,
    VideoCourse,
    VideoCourseCategory,
)


@admin.register(CourseSpecification)
class CourseSpecificationAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "name",
        "description",
        "photo",
    )
    list_display = ("name", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "name",
        "description",
        "teacher",
        "course_specification",
        "start_date",
        "end_date",
        "course_assessment_link",
        "knowledge_assessment_link",
        "is_deleted",
    )
    list_display = ("name", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at", "course_specification")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(CourseSchedule)
class CourseScheduleAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "course",
        "teacher",
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "is_complete",
        "is_deleted",
    )
    list_display = ("course", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at", "course", "teacher")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("course__name", "teacher__name")


# class CourseSessionListenerInline(admin.TabularInline):
#     model = CourseSessionListener
#     fields = ("listener",)
#     autocomplete_fields = ("listener",)
#     extra = 0


@admin.register(CourseSession)
class CourseSessionAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "course_schedule",
        "is_deleted",
    )
    list_display = ("course_schedule", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at", "course_schedule")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("course_schedule__course__name",)
    # inlines = (CourseSessionListenerInline,)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "name",
        "description",
        "course",
        "is_deleted",
    )
    list_display = ("name", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at", "course")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("course__name", "name")


@admin.register(VideoCourseCategory)
class VideoCourseCategoryAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "name",
        "description",
        "is_deleted",
    )
    list_display = ("name", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(VideoCourse)
class VideoCourseAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "name",
        "description",
        "video_course_category",
        "link",
        "is_deleted",
    )
    list_display = ("name", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at", "video_course_category")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("name",)
