from django.db import models
from django_fsm import FSMField, transition


class MonitorPost(models.Model):
    state = FSMField(default="applying")

    @transition(field=state, source="applying", target="won")
    def won(self):
        pass

    @transition(field=state, source="applying", target="lost")
    def lost(self):
        pass

    @transition(field=state, source="won", target="lost")
    def not_selected(self):
        pass

    @transition(field=state, source="lost", target="not_selected")
    def withdrawn(self):
        pass
