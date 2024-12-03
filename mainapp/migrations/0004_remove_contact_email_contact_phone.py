# Generated by Django 5.0.6 on 2024-09-28 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(11)]),
        ),
    ]
