from django.db import models

class pokedexDatabase(models.Model) :
    pokemon_name = models.CharField(max_length=30)
    pokemon_level = models.IntegerField(default=0)
    pokemon_height = models.IntegerField(null=True)
    pokemon_move = models.JSONField(default=list, null=True)
    pokemon_image = models.URLField(null=True)

    def __str__(self):
        return self.pokemon_name
