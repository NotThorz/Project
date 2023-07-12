from django.shortcuts import render, redirect,get_object_or_404
from django.utils.crypto import get_random_string
from .models import ShortenedURL
from .forms import ShortenedURLForm
from django.http import JsonResponse


def redirect_url(request, short_id):
    shortened_url = get_object_or_404(ShortenedURL, short_id=short_id)
    return redirect(shortened_url.original_url)

def shorten_url(request):
    if request.method == 'POST':
        form = ShortenedURLForm(request.POST)
        if form.is_valid():
            short_id = get_random_string(length=6)
            while ShortenedURL.objects.filter(short_id=short_id).exists():
                short_id = get_random_string(length=6)

            shortened_url = form.save(commit=False)
            shortened_url.short_id = short_id
            shortened_url.save()

            new_url = f'{request.scheme}://{request.get_host()}/{short_id}'
            return JsonResponse({'new_url': new_url})
    else:
        form = ShortenedURLForm()

    return render(request, 'shorten_url.html', {'form': form})
