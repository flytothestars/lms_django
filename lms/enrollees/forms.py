from django import forms
from modeltranslation.forms import TranslationModelForm

from enrollees.models import TempEnrollee


class OtherSelect(forms.Select):
    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )
        if value:
            option["attrs"]["data-other"] = str(value.instance.is_other)
        return option


class TempEnrolleeForm(TranslationModelForm, forms.Form):
    class Meta:
        model = TempEnrollee

        # select dropdown
        dropdown_customers = [
            ('до 10', 'до 10'),
            ('от 11 до 30', 'от 11 до 30'),
            ('от 31 до 50', 'от 31 до 50'),
            ('более 51', 'более 51'),
        ]
        dropdown_clients = [
            ('до 5 000 тенге','до 5 000 тенге'),
            ('от 5 001 до 20 000','от 5 001 до 20 000'),
            ('от 20 001 до 50 000','от 20 001 до 50 000'),
            ('от 50 001 до 100 000','от 50 001 до 100 000'),
            ('от 100 001 до 500 000','от 100 001 до 500 000'),
            ('от 500 001 до 1 000 000','от 500 001 до 1 000 000'),
            ('более 1 000 000','более 1 000 000'),
        ]
        fields = [
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
            "course_type",
            "lang",
            "promo_code",
        ]
        widgets = {
            "automation_system": OtherSelect,
            "problem_or_task": OtherSelect,
            "participation_purpose": OtherSelect,
            "is_recording_average_check": forms.Select(choices=dropdown_clients),
            "is_recording_customers": forms.Select(choices=dropdown_customers)
        }
