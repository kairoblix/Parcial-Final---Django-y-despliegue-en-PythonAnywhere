from django.contrib import admin

from .models import Programa


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "facultad", "estado")
    list_filter = ("estado", "facultad")
    search_fields = ("codigo", "nombre", "facultad")
