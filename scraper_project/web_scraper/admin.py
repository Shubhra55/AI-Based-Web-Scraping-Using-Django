from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ScrapedWebsite

@admin.register(ScrapedWebsite)
class ScrapedWebsiteAdmin(admin.ModelAdmin):
    list_display = ("url", "title", "category", "scraped_at")
    search_fields = ("url", "title", "category")
    ordering = ("-scraped_at",)

