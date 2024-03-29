from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import urlshortener

import string
import random

def shorten_url(request):
    if request.method == 'POST':
        full_url = request.POST['full_url']
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

        url_obj = all(original_url=full_url, short_url=short_url)
        url_obj.save()

        return HttpResponse(short_url)

def redirect_to_original(request, short_url):
    url_obj = get_object_or_404(all, short_url=short_url)
    url_obj.visit_count += 1
    url_obj.save()
    return redirect(url_obj.original_url)


from rest_framework import generics
from .models import urlshortener
from .serializers import urlshortenerSerializer

class URLShortenerListCreate(generics.ListCreateAPIView):
    queryset = urlshortener.objects.all()
    serializer_class = urlshortenerSerializer

class URLShortenerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = urlshortener.objects.all()
    serializer_class = urlshortenerSerializer
