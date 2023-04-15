from django.db import models
from django.contrib.auth.models import User


class UrlShortener(models.Model):

    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    main_url = models.CharField(max_length=250)
    short_url = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self