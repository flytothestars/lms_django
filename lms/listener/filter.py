from django_filters import rest_framework

from listener.models import Listener


class ListenerFilter(rest_framework.FilterSet):
    class Meta:
        model = Listener
        fields = [
            "uuid",
        ]
