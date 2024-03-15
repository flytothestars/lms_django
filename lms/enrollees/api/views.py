from rest_framework import generics
from rest_framework.generics import get_object_or_404
from velait.velait_django.main.api.pagination import VelaitPagination
from velait.velait_django.main.api.views import SearchView

from enrollees.api.serializers import EnrolleeSerializer
from enrollees.models import Enrollee


class EnrolleeListAPIView(generics.CreateAPIView, SearchView):
    model = Enrollee
    queryset = Enrollee.objects.all()
    serializer_class = EnrolleeSerializer
    pagination_class = VelaitPagination


class EnrolleeDetailAPIView(
    generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    queryset = Enrollee.objects.all()
    serializer_class = EnrolleeSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), uuid=self.kwargs.get("uuid"))
