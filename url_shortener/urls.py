from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url, name='shorten_url'),
    # Add the redirect URL pattern
    path('<str:short_id>/', views.redirect_url, name='redirect_url'),
]

