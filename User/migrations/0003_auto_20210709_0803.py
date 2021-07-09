# Generated by Django 3.2.4 on 2021-07-09 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20210708_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.AddField(
            model_name='member',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='invited',
            field=models.BooleanField(default=False),
        ),
    ]