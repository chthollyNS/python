# Generated by Django 2.0.1 on 2019-06-14 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190613_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='number',
            field=models.PositiveIntegerField(max_length=100),
        ),
    ]