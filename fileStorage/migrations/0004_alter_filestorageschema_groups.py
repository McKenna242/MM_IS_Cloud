# Generated by Django 3.2.4 on 2021-07-15 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileStorage', '0003_filestorageschema_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filestorageschema',
            name='groups',
            field=models.CharField(default='PRIVATE', max_length=50),
        ),
    ]
