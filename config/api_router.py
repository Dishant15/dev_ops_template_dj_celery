# from django.conf import settings
# from rest_framework.routers import DefaultRouter
# from rest_framework.routers import SimpleRouter

# router = DefaultRouter() if settings.DEBUG else SimpleRouter()


# app_name = "api"
# urlpatterns = router.urls
from django.urls import path, include

urlpatterns = [
    path("user/", include("dev_ops.userapp.urls")),
]