# Generated by Django 3.2 on 2021-05-31 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_villa', '0002_auto_20210531_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
    ]
