from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_id = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
