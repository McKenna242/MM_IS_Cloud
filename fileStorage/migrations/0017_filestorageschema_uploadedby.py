# Generated by Django 3.2.4 on 2021-06-09 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileStorage', '0016_filestorageschema_fileurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='filestorageschema',
            name='uploadedBy',
            field=models.CharField(default='ADMIN', max_length=50),
        ),
    ]
