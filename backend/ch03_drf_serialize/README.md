```sh
- モデルシリアライザーを実行してみる
$ docker compose exec web uv run python manage.py show_serializer
$ docker compose exec web uv run python manage.py create_by_serializer
$ docker compose exec web uv run python manage.py update_by_serializer
```

### Django Shell を実行
```sh
$ docker compose exec web uv run python manage.py shell

>>> from ch03_drf_serialize.model_serializer.models import BlogSerializer
>>> print(BlogSerializer)

>>> from ch03_drf_serialize.model_serializer.models import BlogSerializer
>>> input_data = {
        "title": "new blog title",
        "content": "this is content",
        "author": 1
    }
>>> new_blog = BlogSerializer(data=input_data)
>>> new_blog.is_valid()
>>> new_blog.save()
```
