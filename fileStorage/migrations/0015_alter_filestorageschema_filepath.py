# Generated by Django 3.2.4 on 2021-06-04 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileStorage', '0014_auto_20210604_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filestorageschema',
            name='filePath',
            field=models.FileField(upload_to='F:/School/Summer2021/Independent Study/media/files'),
        ),
    ]
