# Generated by Django 4.0.6 on 2022-07-28 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question',
        ),
    ]
