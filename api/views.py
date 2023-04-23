from django.shortcuts import redirect
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UrlShortenerSerializers
from .models import UrlShortener
from django.views import View
from django.conf import settings
from .permissions import IsLogin


class CreateShortUrl(CreateAPIView):
    serializer_class = UrlShortenerSerializers
    permission_classes = [IsLogin]


class ListShortUrl(ListAPIView):

    # user = User.objects.filter()
    # queryset = UrlShortener.objects.filter(creator=)
    serializer_class = UrlShortenerSerializers
    permission_classes = [IsLogin]

    def get_queryset(self):
        user = self.request.user
        queryset = UrlShortener.objects.filter(creator=user.id)
        return queryset


class Redirect(View):

    def get(self, request, short_link, *args, **kwargs):
        short_link = settings.HOST_URL + "/" + self.kwargs['short_link']
        redirect_link = UrlShortener.objects.filter(short_url=short_link).first().main_url
        return redirect(redirect_link)
