# Generated by Django 5.0.6 on 2024-09-30 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='subject',
        ),
    ]
