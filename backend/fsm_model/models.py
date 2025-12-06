from django.db import models
from django_fsm import FSMField, transition


class MonitorPost(models.Model):
    title = models.CharField(max_length=100)
    state = FSMField(default="応募中")

    def __str__(self):
        return self.title

    @transition(
        field=state, source="応募中", target="当選", custom={"button_name": "当選"}
    )
    def won(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=state, source="応募中", target="落選", custom={"button_name": "落選"}
    )
    def lost(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=state, source="当選", target="不採用", custom={"button_name": "不採用"}
    )
    def not_selected(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=state, source="当選", target="辞退", custom={"button_name": "辞退"}
    )
    def withdrawn(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """
