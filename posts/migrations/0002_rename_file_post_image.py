# Generated by Django 5.1.1 on 2024-09-26 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='file',
            new_name='image',
        ),
    ]