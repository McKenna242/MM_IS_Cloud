# Generated by Django 3.2.4 on 2021-06-03 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileStorage', '0003_rename_filestorage_filestorageschema'),
    ]

    operations = [
        migrations.AddField(
            model_name='filestorageschema',
            name='filePath',
            field=models.FilePathField(default=''),
        ),
    ]
