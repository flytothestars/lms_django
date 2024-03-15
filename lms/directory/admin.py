from django.contrib import admin
from modeltranslation.admin import TranslationAdmin  # noqa

from directory.models import (
    Activity,
    ActivityCategory,
    AutomationSystem,
    ParticipationPurpose,
    ProblemOrTask,
)


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "name",
        "is_deleted",
    )
    list_display = ("name", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "name",
        "activity_category",
        "is_deleted",
    )
    list_display = ("name", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at", "activity_category")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("name", "activity_category__name")


@admin.register(AutomationSystem)
class AutomationSystemAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "name",
        "is_other",
        "is_deleted",
    )
    list_display = ("name", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(ProblemOrTask)
class ProblemOrTaskAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "name",
        "is_deleted",
    )
    list_display = ("name", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(ParticipationPurpose)
class ParticipationPurposeAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "name",
        "is_deleted",
    )
    list_display = ("name", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("name",)
