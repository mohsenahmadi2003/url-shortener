from django.contrib import admin
from django.urls import path, include
from api.views import Redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('<str:short_link>/', Redirect.as_view(), name='redirect'),
    path('api-auth/', include('rest_framework.urls')),
]
