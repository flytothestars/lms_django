from rest_framework import generics
from rest_framework.generics import get_object_or_404
from velait.velait_django.main.api.pagination import VelaitPagination
from velait.velait_django.main.api.views import SearchView

from listener.api.serializers import ListenerSerializer
from listener.models import Listener


class ListenerListAPIView(generics.CreateAPIView, SearchView):
    model = Listener
    queryset = Listener.objects.all()
    serializer_class = ListenerSerializer
    pagination_class = VelaitPagination


class ListenerDetailAPIView(
    generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    queryset = Listener.objects.all()
    serializer_class = ListenerSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), uuid=self.kwargs.get("uuid"))
