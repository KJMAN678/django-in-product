from django.contrib import admin

from blog.models import Blog, CoverImage, Tag

admin.site.register(Blog)
admin.site.register(CoverImage)
# admin.site.register(BlogTag)
admin.site.register(Tag)
