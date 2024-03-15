from django.contrib import admin

from listener.models import Listener


@admin.register(Listener)
class ListenerAdmin(admin.ModelAdmin):
    fields = ("created_at", "updated_at", "user")
    list_display = ("uuid", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at")
    readonly_fields = ("uuid", "created_at", "updated_at")
    search_fields = ("name",)
