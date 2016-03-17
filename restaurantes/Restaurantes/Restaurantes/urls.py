from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^app_restaurante/', include('app_restaurante.urls')),
    url(r'^admin/', admin.site.urls),
    ....
]
