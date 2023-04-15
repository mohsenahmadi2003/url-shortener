from rest_framework.serializers import ModelSerializer
from .models import UrlShortener

class UrlShortenerSerializers(ModelSerializer):
    class Meta:
        model = UrlShortener
        fields = "__all__"