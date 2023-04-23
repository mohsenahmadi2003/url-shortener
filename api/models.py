from django.db import models
from django.contrib.auth.models import User
from random import choices
from string import ascii_letters
from django.conf import settings


class UrlShortener(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    main_url = models.URLField()
    short_url = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def url_shortener():
        while True:
            link = settings.HOST_URL + "/" + "".join(choices(ascii_letters, k=10))
            if not UrlShortener.objects.filter(short_url=link).exists():
                break
        return link

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.url_shortener()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
