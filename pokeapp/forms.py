from django import forms

class TypeSelectionForm(forms.Form):
    type_choices = [('','Select a Pokemon Type'),        
                    ('normal', 'Normal'),
                    ('fighting', 'Fighting'),
                    ('flying', 'Flying'),
                    ('poison', 'Poison'),
                    ('ground', 'Ground'),
                    ('rock', 'Rock'),
                    ('bug', 'Bug'),
                    ('ghost', 'Ghost'),
                    ('steel', 'Steel'),
                    ('fire', 'Fire'),
                    ('water', 'Water'),
                    ('grass', 'Grass'),
                    ('electric', 'Electric'),
                    ('psychic', 'Psychic'),
                    ('ice', 'Ice'),
                    ('dragon', 'Dragon'),
                    ('dark', 'Dark'),
                    ('fairy', 'Fairy'),]
    
    pokemon_type = forms.ChoiceField(choices= type_choices, required=False, label='Select a Pokemon Type : ')


class Pokemons(forms.Form):
    pokemon_choices = [('', 'Select a Pokemon'),
                       ('pidgey', 'Pidgey'),
                       ('rattata', 'Rattata'),
                       ('jigglypuff', 'Jigglypuff'),
                       ('ditto', 'Ditto'),
                       ('eevee', 'Eevee'),
                       ('porygon', 'Porygon'),
                       ('hoothoot', 'Hoothoot'),
                       ('mankey', 'Mankey'),
                       ('primeape', 'Primeape'),
                       ('machop', 'Machop'),
                       ('hitmonchan', 'Hitmonchan'),
                       ('charizard', 'Charizard'),
                       ('pidgeotto', 'Pidgeotto'),
                       ('spearow', 'Spearow'),
                       ('articuno', 'Articuno'),
                       ('zapdos', 'Zapdos'),
                       ('crobat', 'Crobat'),
                       ('ivysaur', 'Ivysaur'),
                       ('gastly', 'Gastly'),
                       ('golem', 'Golem'),
                       ('rhydon', 'Rhydon'),
                       ('groudon', 'Groudon'),
                       ('shieldon', 'Shieldon'),
                       ('caterpie', 'Caterpie'),
                       ('beautifly', 'Beautifly'),
                       ('kricketot', 'Kricketot'),
                       ('duskull', 'Duskull'),
                       ('spiritomb', 'Spiritomb'),
                       ('rotom', 'Rotom'),
                       ('magnemite', 'Magnemite'),
                       ('jirachi', 'Jirachi'),
                       ('lucario', 'Lucario'),
                       ('charmander', 'Charmander'),
                       ('rapidash', 'Rapidash'),
                       ('magmortar', 'Magmortar'),
                       ('lampent', 'Lampent'),
                       ('chandelure', 'Chandelure'),
                       ('squirtle', 'Squirtle'),
                       ('seel', 'Seel'),
                       ('poliwrath', 'Poliwrath'),
                       ('horsea', 'Horsea'),
                       ('bulbasaur', 'Bulbasaur'),
                       ('parasect', 'Parasect'),
                       ('chikorita', 'Chikorita'),
                       ('jumpluff', 'Jumpluff'),
                       ('pikachu', 'Pikachu'),
                       ('electrode', 'Electrode'),
                       ('flaaffy', 'Flaaffy'),
                       ('pachirisu', 'Pachirisu'),
                       ('hypno', 'Hypno'),
                       ('mewtwo', 'Mewtwo'),
                       ('wobbuffet', 'Wobbuffet'),
                       ('swoobat', 'Swoobat'),
                       ('glalie', 'Glalie'),
                       ('walrein', 'Walrein'),
                       ('beartic', 'Beartic'),
                       ('rayquaza', 'Rayquaza'),
                       ('zweilous', 'Zweilous'),
                       ('tyrunt', 'Tyrunt'),
                       ('sneasel', 'Sneasel'),
                       ('carvanha', 'Carvanha'),
                       ('honchkrow', 'Honchkrow'),
                       ('drapion', 'Drapion'),
                       ('clefairy', 'Clefairy'),
                       ('mawile', 'Mawile'),
                       ]
    
    pokemon_names = forms.ChoiceField(choices= pokemon_choices, required=False, label='Select a Pokemon  ')


class Game(forms.Form):
    battle_choices = [('', 'Select a Pokemon'),
                       ('pidgey', 'Pidgey'),
                       ('rattata', 'Rattata'),
                       ('jigglypuff', 'Jigglypuff'),
                       ('ditto', 'Ditto'),
                       ('eevee', 'Eevee'),
                       ('porygon', 'Porygon'),
                       ('hoothoot', 'Hoothoot'),
                       ('mankey', 'Mankey'),
                       ('primeape', 'Primeape'),
                       ('machop', 'Machop'),
                       ('hitmonchan', 'Hitmonchan'),
                       ('charizard', 'Charizard'),
                       ('pidgeotto', 'Pidgeotto'),
                       ('spearow', 'Spearow'),
                       ('articuno', 'Articuno'),
                       ('zapdos', 'Zapdos'),
                       ('crobat', 'Crobat'),
                       ('ivysaur', 'Ivysaur'),
                       ('gastly', 'Gastly'),
                       ('golem', 'Golem'),
                       ('rhydon', 'Rhydon'),
                       ('groudon', 'Groudon'),
                       ('shieldon', 'Shieldon'),
                       ('caterpie', 'Caterpie'),
                       ('beautifly', 'Beautifly'),
                       ('kricketot', 'Kricketot'),
                       ('duskull', 'Duskull'),
                       ('spiritomb', 'Spiritomb'),
                       ('rotom', 'Rotom'),
                       ('magnemite', 'Magnemite'),
                       ('jirachi', 'Jirachi'),
                       ('lucario', 'Lucario'),
                       ('charmander', 'Charmander'),
                       ('rapidash', 'Rapidash'),
                       ('magmortar', 'Magmortar'),
                       ('lampent', 'Lampent'),
                       ('chandelure', 'Chandelure'),
                       ('squirtle', 'Squirtle'),
                       ('seel', 'Seel'),
                       ('poliwrath', 'Poliwrath'),
                       ('horsea', 'Horsea'),
                       ('bulbasaur', 'Bulbasaur'),
                       ('parasect', 'Parasect'),
                       ('chikorita', 'Chikorita'),
                       ('jumpluff', 'Jumpluff'),
                       ('pikachu', 'Pikachu'),
                       ('electrode', 'Electrode'),
                       ('flaaffy', 'Flaaffy'),
                       ('pachirisu', 'Pachirisu'),
                       ('hypno', 'Hypno'),
                       ('mewtwo', 'Mewtwo'),
                       ('wobbuffet', 'Wobbuffet'),
                       ('swoobat', 'Swoobat'),
                       ('glalie', 'Glalie'),
                       ('walrein', 'Walrein'),
                       ('beartic', 'Beartic'),
                       ('rayquaza', 'Rayquaza'),
                       ('zweilous', 'Zweilous'),
                       ('tyrunt', 'Tyrunt'),
                       ('sneasel', 'Sneasel'),
                       ('carvanha', 'Carvanha'),
                       ('honchkrow', 'Honchkrow'),
                       ('drapion', 'Drapion'),
                       ('clefairy', 'Clefairy'),
                       ('mawile', 'Mawile'),
                       ]
    
    fighting_pokemons = forms.MultipleChoiceField(choices=battle_choices, required=False, widget=forms.CheckboxSelectMultiple, label='Select 2 Pokémons ')


# Create your models here.
# pokemon name charfield
# pokemon level  integerfield
# pokemon height https://pokeapi.co/api/v2/pokemon/{id or name}/ integerfield
# pokemon moves slug field
# pokemon sprites https://pokeapi.co/api/v2/pokemon/{id or name}/  imagefield


# login credentials :
# username : pokemons
# email : poke@gmail.com
# password : pikachucute

#create a form to get name of the pokemon. Use its value in different functions(height, img, move) created in views.py

#create a form. Choose to pokemons, if not present in the database fetch and store. 
# Display two pokemons side by side. compare their levels
#https://pokeapi.co/api/v2/type/{id or name}/ -> damage relations -> 