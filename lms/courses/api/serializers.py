from rest_framework import serializers

from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "uuid",
            "created_at",
            "updated_at",
            "name",
            "description",
            "teacher_id",
            "course_assessment_link",
            "knowledge_assessment_link",
        )
