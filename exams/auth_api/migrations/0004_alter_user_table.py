# Generated by Django 5.1.6 on 2025-02-18 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0003_remove_user_last_login'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
