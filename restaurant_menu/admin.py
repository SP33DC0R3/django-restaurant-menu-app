from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status", "author")
    list_filter = ("status", "author")
    search_fields = ("meal", "ingredients")


admin.site.register(Item, MenuItemAdmin)