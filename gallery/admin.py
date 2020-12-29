from django.contrib import admin
from .models import Images


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "created")
    list_filter = ("created",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


