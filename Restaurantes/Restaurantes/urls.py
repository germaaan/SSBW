from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app/', include('app_restaurantes.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^ng-test/$', TemplateView.as_view(template_name='ng_test.html')),
]
