from enum import unique
from django.db.models import fields
from rest_framework import serializers 
from .models import Url

class UrlCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['origin_url',]
        extra_kwargs = {
            'origin_url': {'validators': []},
        }
