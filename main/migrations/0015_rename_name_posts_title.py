# Generated by Django 4.0.3 on 2022-04-29 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_delete_postes_rename_title_posts_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='name',
            new_name='title',
        ),
    ]