from django.conf import settings
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from courses.api.views import CourseDetailAPIView, CourseListAPIView
from enrollees.api.views import EnrolleeDetailAPIView, EnrolleeListAPIView
from listener.api.views import ListenerDetailAPIView, ListenerListAPIView
from teachers.api.views import TeacherDetailAPIView, TeacherListAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="LMS API",
        default_version="v1",
        description="API for LMS project",
    ),
    url=settings.SITE_URL,
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
    patterns=[
        re_path(r"^api/(?P<version>(v1))/", include("lms.api_urls")),
    ],
)

app_name = "api"
urlpatterns = [
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="docs"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path("courses/", CourseListAPIView.as_view()),
    path("courses/<str:uuid>/", CourseDetailAPIView.as_view()),
    path("enrollees/", EnrolleeListAPIView.as_view()),
    path("enrollees/<str:uuid>/", EnrolleeDetailAPIView.as_view()),
    path("listeners/", ListenerListAPIView.as_view()),
    path("listeners/<str:uuid>/", ListenerDetailAPIView.as_view()),
    path("teachers/", TeacherListAPIView.as_view()),
    path("teachers/<str:uuid>/", TeacherDetailAPIView.as_view()),
]
