from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<operator>\w+)/$', views.ProcessPayment.as_view()),
]