from django_filters import rest_framework

from courses.models import Course


class CourseFilter(rest_framework.FilterSet):
    class Meta:
        model = Course
        fields = [
            "uuid",
            "name",
        ]
