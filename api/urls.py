from django.urls import path
from .views import CreateShortUrl, ListShortUrl

app_name = "api"

urlpatterns = [
    path('create/', CreateShortUrl.as_view(), name='create-links'),
    path('list/', ListShortUrl.as_view(), name='list-links'),
]
