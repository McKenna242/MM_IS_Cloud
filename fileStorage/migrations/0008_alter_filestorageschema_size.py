# Generated by Django 3.2.4 on 2021-06-04 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileStorage', '0007_auto_20210603_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filestorageschema',
            name='size',
            field=models.CharField(default='0', max_length=50),
        ),
    ]