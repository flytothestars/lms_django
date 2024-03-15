from rest_framework import serializers

from enrollees.models import Enrollee


class EnrolleeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollee
        fields = (
            "uuid",
            "created_at",
            "updated_at",
            "listener",
            "link",
            "comment",
        )
