from django.db import models
from django_fsm import GET_STATE, FSMField, transition


class MonitorPostState(models.TextChoices):
    applying = "applying", "応募中"
    won = "won", "当選"
    lost = "lost", "落選"
    not_selected = "not_selected", "不採用"
    withdrawn = "withdrawn", "辞退"


class MonitorPost(models.Model):
    title = models.CharField(max_length=100)
    state = FSMField(
        default=MonitorPostState.applying, choices=MonitorPostState.choices
    )

    def __str__(self):
        return self.title

    @transition(
        field=state,
        source=[
            MonitorPostState.won,
            MonitorPostState.lost,
            MonitorPostState.withdrawn,
            MonitorPostState.not_selected,
        ],
        target=MonitorPostState.applying,
        custom={"button_name": "リセット"},
    )
    def reset(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=state,
        source=MonitorPostState.applying,
        target=MonitorPostState.won,
        custom={"button_name": "当選"},
    )
    def won(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=state,
        source=MonitorPostState.applying,
        target=MonitorPostState.lost,
        custom={"button_name": "落選"},
    )
    def lost(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=state,
        source=MonitorPostState.won,
        target=MonitorPostState.not_selected,
        custom={"button_name": "不採用"},
    )
    def not_selected(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=state,
        source=MonitorPostState.won,
        target=MonitorPostState.withdrawn,
        custom={"button_name": "辞退"},
    )
    def withdrawn(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """
