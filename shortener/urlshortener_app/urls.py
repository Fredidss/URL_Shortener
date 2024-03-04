from django.urls import path
from .views import shorten_url, redirect_to_original
from .views import urlshortenerListCreate, URLShortenerRetrieveUpdateDestroy

urlpatterns = [
    path('shorten/', shorten_url, name='shorten_url'),
    path('<str:short_url>/', redirect_to_original, name='redirect_to_original'),
]

urlpatterns = [
    path('api/urls/', urlshortenerListCreate.as_view(), name='urlshortener-list-create'),
    path('api/urls/<int:pk>/', URLShortenerRetrieveUpdateDestroy.as_view(), name='urlshortener-detail'),
]
