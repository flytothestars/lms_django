from django.core.exceptions import ImproperlyConfigured

from courses.models import CourseSpecification


class BasePageMixin:
    title = None
    nav_section = None
    nav_tab = None

    def get_title(self):
        if self.title is not None:
            return self.title
        else:
            raise ImproperlyConfigured('You must provide "title" variable.')

    def get_nav_section(self):
        if self.nav_section is not None:
            return self.nav_section
        else:
            raise ImproperlyConfigured('You must provide "nav_section" variable.')

    def get_nav_tab(self):
        if self.nav_tab is not None:
            return self.nav_tab
        else:
            raise ImproperlyConfigured('You must provide "nav_tab" variable.')

    def get_previous_page(self):
        previous = self.request.GET.get("previous", None)
        return previous

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        context["no_data_msg"] = "-"
        # context["nav_list"] = NAV_LIST
        course_specifications = CourseSpecification.objects.all()
        context["course_specifications"] = course_specifications
        context["nav_section"] = self.get_nav_section()
        context["nav_tab"] = self.get_nav_tab()
        context["previous"] = self.get_previous_page()
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


class FilterMixin:
    filter_class = None

    def get_filter_class(self):
        return self.filter_class

    def get_filter(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return self.get_filter_class()(
            self.request.GET, queryset=qs, request=self.request
        )

    def get_queryset(self, *args, **kwargs):
        return self.get_filter(*args, **kwargs).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.get_filter()
        return context


class SelectRelatedMixin:
    select_related = None

    def get_select_related(self):
        if self.select_related is None:
            raise ImproperlyConfigured("Select related fields must be specified.")
        return self.select_related

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.select_related(*self.get_select_related())
        return queryset


class PrefetchRelatedMixin:
    prefetch_related = None

    def get_prefetch_related(self):
        if self.prefetch_related is None:
            raise ImproperlyConfigured("Prefetch related fields must be specified.")
        return self.prefetch_related

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.prefetch_related(*self.get_prefetch_related())
        return queryset
