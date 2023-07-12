from django.contrib import admin
from .models import ShortenedURL

class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_id', 'created_at')
    search_fields = ('original_url', 'short_id')

admin.site.register(ShortenedURL, ShortenedURLAdmin)
