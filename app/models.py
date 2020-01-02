from django.db import models


class Event(models.Model):
    TYPE_CHOICES = (
        (1, '練習'),
        (2, '試合'),
        (3, '飲み会'),
        (4, '合宿'),
        (5, 'グリトマカップ'),
        (6, 'その他イベント'),
    )

    name = models.CharField(
        verbose_name='イベント名',
        max_length=20,
    )
    type = models.IntegerField(
        verbose_name='種類',
        choices=TYPE_CHOICES,
        default=1
    )
    date = models.DateTimeField(
        verbose_name='日時',
    )
    place = models.CharField(
        verbose_name='場所',
        max_length=50,
    )
    memo = models.TextField(
        verbose_name='詳細',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'イベント'
        verbose_name_plural = 'イベント'


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    comment_text = models.TextField()

    class Meta:
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント'
