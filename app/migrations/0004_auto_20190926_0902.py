# Generated by Django 2.2.5 on 2019-09-26 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'コメント', 'verbose_name_plural': 'コメント'},
        ),
    ]
