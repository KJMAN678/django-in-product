from django.contrib import admin

from ch02_orm.bulk_create_trouble.models import (
    BaseModel,
    ChildModel,
    ManyToManyModel,
    OneModel,
    SampleModel,
    SignalTriggerModel,
)

admin.site.register(SignalTriggerModel)
admin.site.register(SampleModel)
admin.site.register(ManyToManyModel)
admin.site.register(OneModel)
admin.site.register(BaseModel)
admin.site.register(ChildModel)
