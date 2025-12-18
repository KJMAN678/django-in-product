from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("<version>/api/", include("ch01_drf.api.urls")),
    path("async/", include("ch02_orm.async.urls")),
]
