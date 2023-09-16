from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse, HttpResponse

def hello(request):
    return render(request, 'index.html')
    #return HttpResponse('Hello! Welcome to Pokedex')

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
        
        #return JsonResponse({'pokemon_types': types})
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
        
        #return JsonResponse({'pokemon_versions': dversion})
        return render(request, 'versions.html', dversion)
    except Exception as e:
        return JsonResponse({'error': str(e)})
    

def pokemon_ability(request):
    # API endpoint for Pokémon ability
    version_url = 'https://pokeapi.co/api/v2/ability/' 

    try:
        # Fetch data from the PokeAPI
        response = requests.get(version_url)
        data = response.json()
        
        # Extract the list of Pokémon ability
        ability = [ability_info['name'] for ability_info in data['results']]
        dability = {'pokemon_ability': ability}
        
        #return JsonResponse({'pokemon_ability': dability})
        return render(request, 'ability.html', dability)
    except Exception as e:
        return JsonResponse({'error': str(e)})