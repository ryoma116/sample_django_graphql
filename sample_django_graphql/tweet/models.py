from account.models import Account
from django.db import models


class Tweet(models.Model):
    text = models.CharField("本文", max_length=100)
    account = models.ForeignKey(
        Account,
        verbose_name="アカウント",
        related_name="tweets",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = verbose_name_plural = "ツイート"
        db_table = "tweet"
