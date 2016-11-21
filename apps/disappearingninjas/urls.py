from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^ninjas/$', views.showall),
    url(r'^ninjas/(?P<color>\w+)$', views.show),
    url(r'^', views.index),
]
