# Generated by Django 4.1.3 on 2023-07-05 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_service_delete_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='name',
        ),
    ]