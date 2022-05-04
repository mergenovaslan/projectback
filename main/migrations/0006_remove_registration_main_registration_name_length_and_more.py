# Generated by Django 4.0.3 on 2022-04-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_registration_main_registration_title_length_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='registration',
            name='main_registration_name_length',
        ),
        migrations.AddConstraint(
            model_name='registration',
            constraint=models.CheckConstraint(check=models.Q(('name__length__gte', 5)), name='main_registration_name_length'),
        ),
    ]