from django.urls import path
from . import views


urlpatterns = [
path('', views.hello, name='hello'),
path('types/', views.pokemon_types, name='pokemon types'),
path('versions/', views.pokemon_versions, name='pokemon versions'),
path('ability/', views.pokemon_ability, name='pokemon ability'),
path('typedist/', views.type_distribution, name='types distribution'),
path('details/', views.pokemon_details, name='pokemon details'),
path('details/view/', views.view_details, name='pokemon details'),
path('games/', views.start_battle, name='pokemon games'),
]