from django.urls import path

from .views import test_api

app_name = "userapp"
urlpatterns = [
    path("test/", test_api, name="user-test"),
]