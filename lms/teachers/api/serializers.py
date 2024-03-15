from rest_framework import serializers

from teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            "uuid",
            "created_at",
            "updated_at",
        )
