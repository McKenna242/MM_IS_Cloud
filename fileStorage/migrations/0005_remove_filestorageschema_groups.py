# Generated by Django 3.2.4 on 2021-07-15 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileStorage', '0004_alter_filestorageschema_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filestorageschema',
            name='groups',
        ),
    ]
