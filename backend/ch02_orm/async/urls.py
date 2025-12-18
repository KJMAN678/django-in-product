from django.urls import include, path

from .views import get_blog, get_blog_async

urlpatterns = [
    path("get-blog/", get_blog, name="get-blog"),
    path("get-blog-async/", get_blog_async, name="get-blog-async"),
]
