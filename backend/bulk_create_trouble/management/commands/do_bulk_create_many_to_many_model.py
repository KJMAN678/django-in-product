from django.core.management.base import BaseCommand

from bulk_create_trouble.models import ManyToManyModel, OneModel


class Command(BaseCommand):
    help = "Do bulk create many to many model"

    def handle(self, *args, **options):
        one_models = []
        for i in range(3):
            one_models.append(OneModel.objects.create(name=f"bulk_created_{i}"))

        many_to_many_model = ManyToManyModel.objects.create(name="bulk_created")
        many_to_many_model.many_to_many.set(one_models)

        self.stdout.write(self.style.SUCCESS("ManyToManyModelを作成しました。"))

        many_to_many_models = []
        for i in range(3):
            many_to_many_models.append(ManyToManyModel(name=f"bulk_created_{i}"))

        ManyToManyModel.objects.bulk_create(many_to_many_models)

        many_to_many_through_models = []
        for i in range(3):
            for one_model in one_models:
                many_to_many_through_models.append(
                    ManyToManyModel.many_to_many.through(
                        manytomanymodel_id=many_to_many_models[i].id,
                        # pyrefly: ignore [missing-attribute]
                        onemodel_id=one_model.id,
                    )
                )

        ManyToManyModel.many_to_many.through.objects.bulk_create(
            many_to_many_through_models
        )

        self.stdout.write(self.style.SUCCESS("ManyToManyModelをbulk_createしました。"))
