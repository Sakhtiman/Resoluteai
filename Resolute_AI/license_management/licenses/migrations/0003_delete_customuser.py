# Generated by Django 3.2 on 2024-01-24 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]