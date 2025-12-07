from django.core.management.base import BaseCommand

from bulk_create_trouble.models import SignalTriggerModel


class Command(BaseCommand):
    help = "Do bulk create"

    def handle(self, *args, **options):
        signal_trigger_models = []

        # bulk create はシグナル pre_save が実行されない
        for i in range(3):
            signal_trigger_models.append(
                SignalTriggerModel(
                    name=f"bulk_created_{i}",
                )
            )

        SignalTriggerModel.objects.bulk_create(signal_trigger_models)

        SignalTriggerModel.objects.create(name="created")

        self.stdout.write(
            self.style.SUCCESS(
                "3件 bulk_createを実行、signal は発火せず。1件 created を実行し signal が発火しました。"
            )
        )
