from rest_framework import serializers
from .models import urlshortener

class urlshortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = urlshortener
        fields = ['id', 'original_url', 'short_url', 'visits']
