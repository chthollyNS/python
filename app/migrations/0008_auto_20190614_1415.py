# Generated by Django 2.0.1 on 2019-06-14 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190614_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='read',
            field=models.TextField(default='还未观看小说/还未观看小说/还未观看小说/'),
        ),
    ]
