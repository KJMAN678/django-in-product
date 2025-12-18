from django.db import models

# 循環参照が発生する
# from a_model.models import A1Model


class B1Model(models.Model):
    fieldA = models.CharField(max_length=100)


# 循環参照が発生する
# class B2Model(models.Model):
#     fieldA = models.CharField(max_length=100)
#     fieldB = models.ForeignKey(A1Model)


class B2Model(models.Model):
    fieldA = models.CharField(max_length=100)
    # 文字列で読み込めば循環参照が解決する
    fieldB = models.ForeignKey("a_model.A1Model", on_delete=models.CASCADE)
