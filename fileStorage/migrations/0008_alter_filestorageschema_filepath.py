# Generated by Django 3.2.4 on 2021-07-22 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileStorage', '0007_auto_20210722_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filestorageschema',
            name='filePath',
            field=models.FileField(max_length=255, upload_to='F:/School/Summer2021/Independent Study/media/files'),
        ),
    ]
