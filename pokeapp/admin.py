from django.contrib import admin
from pokeapp.models import pokedexDatabase

# Register your models here.
class pokedexAdmin(admin.ModelAdmin) :
    list_display = ('pokemon_name', 'pokemon_level', 'pokemon_height', 'pokemon_move', 'pokemon_image')


admin.site.register(pokedexDatabase ,pokedexAdmin)
