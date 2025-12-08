from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("<version>/api/", include("api.urls")),
    path("async/", include("async.urls")),
]
