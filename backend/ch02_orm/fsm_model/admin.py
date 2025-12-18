from django.contrib import admin
from django_fsm import transition
from fsm_admin.mixins import FSMTransitionMixin

from ch02_orm.fsm_model.models import MonitorPost


class MonitorPostAdmin(FSMTransitionMixin, admin.ModelAdmin):
    # The name of one or more FSMFields on the model to transition
    fsm_field = [
        "state",
    ]
    readonly_fields = [
        "state",
    ]


admin.site.register(MonitorPost, MonitorPostAdmin)
