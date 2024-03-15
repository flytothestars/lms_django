from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect

from enrollees.models import Enrollee, TempEnrollee


@admin.register(Enrollee)
class EnrolleeAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "listener",
        "link",
        "comment",
        "is_deleted",
    )
    list_display = ("uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("comment",)


@admin.register(TempEnrollee)
class TempEnrolleeAdmin(admin.ModelAdmin):
    fields = (
        "created_at",
        "updated_at",
        "link",
        "full_name",
        "phone_number",
        "email",
        "company_name",
        "identification_number",
        "activity",
        "description",
        "number_of_completed_years",
        "employee_count",
        "is_recording_customers",
        "is_recording_average_check",
        "automation_system",
        "problem_or_task",
        "participation_purpose",
        "lang",
        "promo_code",
        "is_complete_course",
        "is_emailed",
        "email_is_not_valid",
        "is_deleted",
    )
    list_display = ("full_name", "status","uuid", "created_at", "updated_at")
    list_filter = (
        "is_deleted",
        "created_at",
        "updated_at",
        "activity",
    )
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("identification_number", "company_name", "activity")
    change_form_template = "admin/change_form.html"