from django.urls import include, path

from .views import async_view_with_transaction, get_blog, get_blog_async

urlpatterns = [
    path("get-blog/", get_blog, name="get-blog"),
    path("get-blog-async/", get_blog_async, name="get-blog-async"),
    path(
        "async-view-with-transaction/",
        async_view_with_transaction,
        name="async-view-with-transaction",
    ),
]
