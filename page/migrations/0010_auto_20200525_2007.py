# Generated by Django 3.0.3 on 2020-05-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_auto_20200524_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
