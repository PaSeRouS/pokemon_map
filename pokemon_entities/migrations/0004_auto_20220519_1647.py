# Generated by Django 2.2.24 on 2022-05-19 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20220518_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='disapperead_at',
            new_name='disappeared_at',
        ),
    ]
