# Generated by Django 3.2 on 2023-05-14 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_project_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='report',
        ),
    ]
