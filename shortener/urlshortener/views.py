from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import URL
import string
import random

def shorten_url(request):
    if request.method == 'POST':
        full_url = request.POST['full_url']
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

        url_obj = URL(original_url=full_url, short_url=short_url)
        url_obj.save()

        return HttpResponse(short_url)

def redirect_to_original(request, short_url):
    url_obj = get_object_or_404(URL, short_url=short_url)
    url_obj.visit_count += 1
    url_obj.save()
    return redirect(url_obj.original_url)
