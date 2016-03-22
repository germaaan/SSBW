from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^app_restaurantes/', include('app_restaurantes.urls')),
    url(r'^admin/', admin.site.urls),
]
