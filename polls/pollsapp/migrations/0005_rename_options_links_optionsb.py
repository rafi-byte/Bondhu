# Generated by Django 4.0.6 on 2022-08-01 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollsapp', '0004_rename_vote_links_vote1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='options',
            new_name='optionsb',
        ),
    ]
