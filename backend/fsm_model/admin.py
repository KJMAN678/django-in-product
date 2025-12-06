from django.contrib import admin
from fsm_admin.mixins import FSMTransitionMixin

from fsm_model.models import MonitorPost


class MonitorPostAdmin(FSMTransitionMixin, admin.ModelAdmin):
    # The name of one or more FSMFields on the model to transition
    fsm_field = [
        "state",
    ]


admin.site.register(MonitorPost, MonitorPostAdmin)
