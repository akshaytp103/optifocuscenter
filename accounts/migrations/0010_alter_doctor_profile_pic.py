# Generated by Django 4.1.3 on 2023-07-12 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_doctor_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
