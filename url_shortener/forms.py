from django import forms
from .models import ShortenedURL

class ShortenedURLForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['original_url']
        labels = {
            'original_url': 'Enter URL to shorten:',
        }

