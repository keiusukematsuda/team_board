from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    POSITION_CHOICES = (
        (1, "前衛"),
        (2, "後衛"),
    )

    SEX_CHOICES = (
        (1, "男"),
        (2, "女"),
    )

    dspname = models.CharField(
        verbose_name='表示名',
        max_length=10,
    )

    position = models.IntegerField(
        verbose_name='ポジション',
        choices=POSITION_CHOICES,
        default=1,
    )

    sex = models.IntegerField(
        verbose_name='性別',
        choices=SEX_CHOICES,
        default=1,
    )

    # アイコンを画像を保存できるImageFieldとして定義する
    icon = models.ImageField(upload_to="image/", blank=True, null=True)

    # 作成を成功したら'ginstagram:profile'と定義されているURLに飛ぶ
    def get_absolute_url(self):
        return reverse('proto1:event_list')
