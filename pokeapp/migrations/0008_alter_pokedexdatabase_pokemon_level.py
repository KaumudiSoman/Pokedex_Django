# Generated by Django 4.2.5 on 2023-09-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0007_alter_pokedexdatabase_pokemon_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokedexdatabase',
            name='pokemon_level',
            field=models.IntegerField(default=0),
        ),
    ]