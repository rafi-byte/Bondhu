# Generated by Django 4.0.6 on 2022-08-01 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollsapp', '0003_links'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='vote',
            new_name='vote1',
        ),
    ]