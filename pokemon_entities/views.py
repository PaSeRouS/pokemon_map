import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.timezone import localtime

from pokemon_entities.models import Pokemon
from pokemon_entities.models import PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemons_coords = PokemonEntity.objects.filter(
        appeared_at__lt=localtime(),
        disappeared_at__gt=localtime()
    )

    for pokemon in pokemons_coords:
        add_pokemon(
            folium_map, pokemon.lat,
            pokemon.lon,
            pokemon.pokemon.photo.path
        )

    pokemons = Pokemon.objects.all()
    
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemon_photo = None

        if pokemon.photo:
            pokemon_photo = pokemon.photo.url

        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon_photo,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    searched_pokemon = Pokemon.objects.get(id=pokemon_id)

    pokemons_coords = PokemonEntity.objects.filter(
        pokemon=searched_pokemon,
        appeared_at__lt=localtime(),
        disappeared_at__gt=localtime()
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_coords:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            searched_pokemon.photo.path
        )

    pokemon = {}
    pokemon['title_ru'] = searched_pokemon.title
    pokemon['img_url'] = searched_pokemon.photo.url
    pokemon['description'] = searched_pokemon.description
    pokemon['title_en'] = searched_pokemon.title_en
    pokemon['title_jp'] = searched_pokemon.title_jp

    if searched_pokemon.previous_evolution:
        previous_evolution = {}
        previous_evolution['title_ru'] = searched_pokemon.previous_evolution.title
        previous_evolution['pokemon_id'] = searched_pokemon.previous_evolution.id
        previous_evolution['img_url'] = searched_pokemon.previous_evolution.photo.url
        pokemon['previous_evolution'] = previous_evolution

    next_evolutions = searched_pokemon.pokemons.all()

    if next_evolutions:
        next_evolution = {}
        next_evolution['title_ru'] = next_evolutions[0].title
        next_evolution['pokemon_id'] = next_evolutions[0].id
        next_evolution['img_url'] = next_evolutions[0].photo.url
        pokemon['next_evolution'] = next_evolution


    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
