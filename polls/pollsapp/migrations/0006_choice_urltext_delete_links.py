# Generated by Django 4.0.6 on 2022-08-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollsapp', '0005_rename_options_links_optionsb'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='urltext',
            field=models.CharField(default='Some String', max_length=1000),
        ),
        migrations.DeleteModel(
            name='Links',
        ),
    ]