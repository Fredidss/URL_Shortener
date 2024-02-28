from django.db import models
import string
import random

class URLShortener(models.Model):
    original_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=5, unique=True)
    visits = models.IntegerField(default=0)

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(5))
        return short_url

    def record_visit(self):
        self.visits += 1
        self.save()

    @staticmethod
    def get_shortened_urls():
        return URLShortener.objects.all()

    @staticmethod
    def get_url_by_shortened(short_url):
        return URLShortener.objects.get(short_url=short_url)

