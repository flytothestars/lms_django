from rest_framework import generics
from rest_framework.generics import get_object_or_404
from velait.velait_django.main.api.pagination import VelaitPagination
from velait.velait_django.main.api.views import SearchView

from teachers.api.serializers import TeacherSerializer
from teachers.models import Teacher


class TeacherListAPIView(generics.CreateAPIView, SearchView):
    model = Teacher
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = VelaitPagination


class TeacherDetailAPIView(
    generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), uuid=self.kwargs.get("uuid"))
