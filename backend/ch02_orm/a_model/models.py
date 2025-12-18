from django.db import models

# 循環参照が発生する
# from b_model.models import B1Model


# 循環参照が発生する
# class A1Model(models.Model):
#     fieldA = models.CharField(max_length=100)
#     fieldB = models.ForeignKey(B1Model)


class A1Model(models.Model):
    fieldA = models.CharField(max_length=100)
    fieldB = models.ForeignKey("b_model.B1Model", on_delete=models.CASCADE)


class A2Model(models.Model):
    fieldsA = models.CharField(max_length=100)
