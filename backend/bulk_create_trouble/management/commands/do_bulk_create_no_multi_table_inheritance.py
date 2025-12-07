from django.core.management.base import BaseCommand

from bulk_create_trouble.models import ChildModel


class Command(BaseCommand):
    help = "Do bulk create no multi table inheritance"

    def handle(self, *args, **options):
        signal_trigger_models = []

        # bulk create はシグナル pre_save が実行されない
        for i in range(3):
            signal_trigger_models.append(
                ChildModel(
                    name=f"bulk_created_{i}",
                    name_child_only=f"bulk_created_child_{i}",
                )
            )

        try:
            ChildModel.objects.bulk_create(signal_trigger_models)
            self.stdout.write(self.style.SUCCESS("3件 bulk_createを実行しました。"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"bulk_create error: {e}"))

        ChildModel.objects.create(name="created", name_child_only="created_child")

        self.stdout.write(self.style.SUCCESS("1件 created を実行しました。"))
