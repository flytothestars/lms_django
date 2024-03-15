from django.contrib import admin

from teachers.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "user",
        "bio",
        "photo",
        "experience",
        "link",
    )
    list_display = ("user", "uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("user__username",)
