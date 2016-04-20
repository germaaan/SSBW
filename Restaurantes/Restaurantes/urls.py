from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app/', include('app_restaurantes.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
