# Generated by Django 4.0.3 on 2022-04-01 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_tag_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
    ]