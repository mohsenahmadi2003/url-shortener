from rest_framework import serializers
from .models import UrlShortener
from django.contrib.auth.models import User


class UrlShortenerSerializers(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    class Meta:
        model = UrlShortener
        fields = "__all__"
