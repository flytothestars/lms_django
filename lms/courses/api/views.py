from rest_framework import generics
from rest_framework.generics import get_object_or_404
from velait.velait_django.main.api.pagination import VelaitPagination
from velait.velait_django.main.api.views import SearchView

from courses.api.serializers import CourseSerializer
from courses.models import Course


class CourseListAPIView(generics.CreateAPIView, SearchView):
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = VelaitPagination


class CourseDetailAPIView(
    generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), uuid=self.kwargs.get("uuid"))
