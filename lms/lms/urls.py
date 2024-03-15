from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views import defaults as default_views
from core import views
from core.views import AboutPage, IndexPage, KnowledgeBasePage, ExpertPage
from enrollees.views import PrintPdfDetailView, approve_object
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^api/(?P<version>(v1|v2))/", include("lms.api_urls")),
    # re_path(r'^.*$', views.block, name='catch_all')
    path("pdf-print-page/<int:pk>/",PrintPdfDetailView.as_view(),name="pdf-print-page",),
    path("request-success/<int:pk>/",approve_object,name="request-success",),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("i18n/", include("django.conf.urls.i18n")),

]

urlpatterns += i18n_patterns(
    path("courses/", include("courses.urls")),
    path("enrollees/", include("enrollees.urls")),
    path("about/", AboutPage.as_view(), name="about"),
    path("expert/", ExpertPage.as_view(), name="expert"),
    path("knowledge-base/", KnowledgeBasePage.as_view(), name="knowledge-base"),
    path("", IndexPage.as_view(), name="index"),
    
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page Not Found")},
        ),
        path("500/", default_views.server_error),
    ]
