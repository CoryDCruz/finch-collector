# Generated by Django 4.1.1 on 2022-09-27 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='cat',
            new_name='finch',
        ),
    ]
