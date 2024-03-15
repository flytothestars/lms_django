from rest_framework import serializers

from listener.models import Listener


class ListenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listener
        fields = (
            "uuid",
            "created_at",
            "updated_at",
        )
