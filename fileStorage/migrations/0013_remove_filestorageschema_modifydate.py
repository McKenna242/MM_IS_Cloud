# Generated by Django 3.2.4 on 2021-06-04 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileStorage', '0012_auto_20210604_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filestorageschema',
            name='modifyDate',
        ),
    ]
