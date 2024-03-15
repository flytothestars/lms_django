from django.urls import path

from courses.views import CourseList, VideoCourseList

app_name = "courses"
urlpatterns = [
    path(
        "course-list/",
        CourseList.as_view(),
        name="course-list",
    ),
    path(
        "video-course-list/",
        VideoCourseList.as_view(),
        name="video-course-list",
    ),
]
