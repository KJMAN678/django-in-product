from django.http import JsonResponse

from ch02_orm.blog.models import Blog


def get_blog(request):
    blog_details = Blog.objects.get(id=1)
    return JsonResponse({"title": blog_details.title})


async def get_blog_async(request):
    blog_details = await Blog.objects.aget(id=1)
    return JsonResponse({"title": blog_details.title})
