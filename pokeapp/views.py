from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse
from .forms import TypeSelectionForm, Pokemons, Game
from pokeapp.models import pokedexDatabase

def hello(request):
    return render(request, 'index.html')

def pokemon_types(request):
    # API endpoint for Pokémon types
    type_url = 'https://pokeapi.co/api/v2/type/' 

    try:
        # Fetch data from the PokeAPI
        response = requests.get(type_url)
        data = response.json()
        
        # Extract the list of Pokémon types
        types = [type_info['name'] for type_info in data['results']]
        dtypes = {'pokemon_types': types}
        # turls = [turl_info['url'] for turl_info in data['results']]
        # dturls = {'pokemon_turls': turls}
        
        return render(request, 'types.html', dtypes)
    except Exception as e:
        return JsonResponse({'error': str(e)})
    

def pokemon_versions(request):
    # API endpoint for Pokémon versions
    version_url = 'https://pokeapi.co/api/v2/version/' 

    try:
        # Fetch data from the PokeAPI
        response = requests.get(version_url)
        data = response.json()
        
        # Extract the list of Pokémon versions
        version = [version_info['name'] for version_info in data['results']]
        dversion = {'pokemon_versions': version}
        
        return render(request, 'versions.html', dversion)
    except Exception as e:
        return JsonResponse({'error': str(e)})
    

def pokemon_ability(request):
    # API endpoint for Pokémon ability
    ability_url = 'https://pokeapi.co/api/v2/ability/' 

    try:
        # Fetch data from the PokeAPI
        response = requests.get(ability_url)
        data = response.json()
        
        # Extract the list of Pokémon ability
        ability = [ability_info['name'] for ability_info in data['results']]
        dability = {'pokemon_ability': ability}
        
        return render(request, 'ability.html', dability)
    except Exception as e:
        return JsonResponse({'error': str(e)})
    
  

def type_distribution(request):
        
    if request.method == 'POST':
        form1 = TypeSelectionForm(request.POST)

        if form1.is_valid():
            selected_type = form1.cleaned_data['pokemon_type']
            poketype_url = f'https://pokeapi.co/api/v2/type/{selected_type}'

            try:
                #Fetch data from the PokeAPI
                response = requests.get(poketype_url)

                if(response.status_code == 200):
                    data = response.json()
                    # Extract the list of Pokémon types
                    poketype = [poketype_info['pokemon']['name'] for poketype_info in data['pokemon']]
                    dpoketype = {'pokemon_type': poketype}

                    return render(request, 'typenames.html', dpoketype)
                else:
                    return JsonResponse({'error': str(e)})
                
            except Exception as e:
                return JsonResponse({'error': str(e)})
    else:
        form1 = TypeSelectionForm()
    return render(request, 'tydistribution.html', {'form1': form1})



#Takes name of the pokemon, checks whether it already exists in database
def pokemon_details(request):
    if request.method == 'POST':
        form2 = Pokemons(request.POST)

        if form2.is_valid():
            selected_pokemon = form2.cleaned_data['pokemon_names']
            
            if(pokedexDatabase.objects.filter(pokemon_name=selected_pokemon)).exists():
                increment_level(selected_pokemon)
                return render(request, 'saved.html', {'selected_pokemon' : selected_pokemon})
            else:
                data = fetchDetails(selected_pokemon)
                if data:
                    storeDetails(data)
                    return render(request, 'success.html', {'selected_pokemon' : selected_pokemon})
                else:
                    print('error')
    else:
        form2 = Pokemons()
    return render(request, 'details.html', {'form2': form2})



# Takes pokemon name as parameter and fetches its details from api
def fetchDetails(pokemon_name):
    pokemon_details = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
                
    #Fetch data from the PokeAPI
    response = requests.get(pokemon_details)

    if(response.status_code == 200):
        data = response.json()
        return data
    else:
        return None


# Takes fetched data as a parameter and stores it in database using instance of model
def storeDetails(data):
    pokedata = pokedexDatabase(
        pokemon_name = data['name'],
        pokemon_height = data['height'],
        pokemon_move = [moves_info['move']['name'] for moves_info in data['moves']],
        pokemon_image = data['sprites']['front_default'],
    )
    pokedata.save()


#pokemon level increases every time it is cought
def increment_level(pokemon_name):
    try:
        pokedata = pokedexDatabase.objects.get(pokemon_name = pokemon_name)
        pokedata.pokemon_level += 1
        pokedata.save()
    except:
        data = fetchDetails(pokemon_name)
        if data:
            storeDetails(data)
            return render('success.html', {'selected_pokemon' : pokemon_name})
        else:
            print('error')
    

def view_details(request):
    display_all = pokedexDatabase.objects.all()
    print(display_all)
    return render(request, 'view.html', {'display_all' : display_all})



def start_battle(request):
    if request.method == 'POST':
        form3 = Game(request.POST)

        if form3.is_valid():
            battling_pokemons = form3.cleaned_data['fighting_pokemons']
            print(battling_pokemons) 
            pokemon1 = battling_pokemons[0]
            pokemon2 = battling_pokemons[1]

            try:
                if(pokedexDatabase.objects.filter(pokemon_name = battling_pokemons[0])).exists() and (pokedexDatabase.objects.filter(pokemon_name = battling_pokemons[1])).exists():
                    pokemon = pokedexDatabase.objects.get(pokemon_name=pokemon1)
                    level1 = pokemon.pokemon_level
                    pokemon = pokedexDatabase.objects.get(pokemon_name=pokemon2)
                    level2 = pokemon.pokemon_level
                        
                    if level1 > level2:
                        winner = battling_pokemons[0]
                    elif level2 > level1:
                        winner = battling_pokemons[1]
                    else:
                        winner = "It's a tie :("

                    return render(request, 'result.html', {'winner' : winner})
                else:
                    if not (pokedexDatabase.objects.filter(pokemon_name = battling_pokemons[0])).exists():
                        data = fetchDetails(battling_pokemons[0])
                        if data:
                            storeDetails(data)
                            return render(request, 'success.html', {'selected_pokemon' : battling_pokemons[0]})
                        else:
                            print('error')
                    if not (pokedexDatabase.objects.filter(pokemon_name = battling_pokemons[1])).exists():
                        data = fetchDetails(battling_pokemons[1])
                        if data:
                            storeDetails(data)
                            return render(request, 'success.html', {'selected_pokemon' : battling_pokemons[1]})
                        else:
                            print('error')
            
            except Exception as e:
                return JsonResponse({'error': str(e)})
        
    else:
        form3 = Game()
    return render(request, 'startbattle.html', {'form3' : form3})