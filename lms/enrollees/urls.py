from django.urls import path

from enrollees.views import TempEnrolleeCreate

app_name = "enrollees"
urlpatterns = [
    path(
        "temp-enrollee-create/",
        TempEnrolleeCreate.as_view(),
        name="temp-enrollee-create",
    ),
]
