# Generated by Django 2.2.24 on 2022-05-19 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_auto_20220519_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='from_evolved',
            new_name='previous_evolution',
        ),
    ]
