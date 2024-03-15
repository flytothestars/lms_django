from django_filters import rest_framework

from teachers.models import Teacher


class TeacherFilter(rest_framework.FilterSet):
    class Meta:
        model = Teacher
        fields = [
            "uuid",
        ]
