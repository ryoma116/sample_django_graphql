from django.db import models


class Account(models.Model):
    username = models.CharField("ユーザ名", max_length=100)
    name = models.CharField("名前", max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = verbose_name_plural = "アカウント"
        db_table = "account"
