# Generated by Django 5.1.1 on 2024-09-29 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_file_file_alter_post_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
    ]
