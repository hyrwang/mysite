# Generated by Django 2.0 on 2019-08-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20190816_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_id',
            field=models.IntegerField(default=0),
        ),
    ]
