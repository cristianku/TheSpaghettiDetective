# Generated by Django 2.1.7 on 2019-11-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20191110_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dh_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='is_pro',
            field=models.BooleanField(default=True),
        ),
    ]
