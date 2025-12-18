from django.http import JsonResponse

from ch02_orm.blog.models import Blog


def get_blog(request):
    blog_details = Blog.objects.get(id=1)
    return JsonResponse({"title": blog_details.title})


async def get_blog_async(request):
    blog_details = await Blog.objects.aget(id=1)
    return JsonResponse({"title": blog_details.title})


from asgiref.sync import sync_to_async
from django.db import transaction


def _do_in_transaction(user_id: int):
    with transaction.atomic():
        # select_for_update 等、トランザクション前提のORM処理
        blog = Blog.objects.select_for_update().get(id=1)
        blog.title = "hoge"
        blog.save()

    return blog.title


async def async_view_with_transaction(request):
    result = await sync_to_async(_do_in_transaction, thread_sensitive=True)(
        request.user.id
    )
    return JsonResponse({"ok": True, "result": result})
