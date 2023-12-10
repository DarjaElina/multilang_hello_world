from .apps import HelloConfig
from django.urls import path, include
from .views import hello

app_name = HelloConfig.name

urlpatterns = (
    path("", hello, name="index"),
)