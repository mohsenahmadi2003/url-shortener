from rest_framework.serializers import ModelSerializer
from .models import UrlShortener

class urlShortenerSerializer(ModelSerializer):
    class Meta:
        model = UrlShortener
        fields = "__all__"