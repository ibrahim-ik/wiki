# Generated by Django 2.0.6 on 2018-07-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180715_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='last_update',
            field=models.DateTimeField(),
        ),
    ]
