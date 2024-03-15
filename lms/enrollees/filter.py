from django_filters import rest_framework

from enrollees.models import Enrollee


class EnrolleeFilter(rest_framework.FilterSet):
    class Meta:
        model = Enrollee
        fields = [
            "uuid",
        ]
