# Generated by Django 2.0.6 on 2018-07-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optimizer', '0003_auto_20180621_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledactivity',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
