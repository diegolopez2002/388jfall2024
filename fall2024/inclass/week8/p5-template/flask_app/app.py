from flask import Flask, render_template, send_from_directory
import requests
from .model import PokeClient
app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
poke_client = PokeClient()


# We will demonstrate how to fetch using JS in the frontend (server -> client) 
@app.route('/')
def index():
    """
    Must show all of the pokemon names as clickable links

    Check the README for more detail.
    """
    
    return render_template('index.html')


# How to fetch using python requests (server -> server)
@app.route('/pokemon/<pokemon_name>')
def pokemon_info(pokemon_name):
    """
    Must show all the info for a pokemon identified by name

    Check the README for more detail
    """
    
    response = requests.get(f'http://127.0.0.1:5000/get_pokemon_info/{pokemon_name}')
    print(response.json())
    return render_template('pokemon_info.html', info=response.json()['info'], pokemon_name=response.json()['pokemon_name'])

@app.route('/ability/<ability_name>')
def pokemon_with_ability(ability_name):
    """
    Must show a list of pokemon 

    Check the README for more detail
    """
    response = requests.get(f'http://127.0.0.1:5000/get_pokemon_with_ability/{ability_name}')
    print(response.json())
    return render_template('pokemon_with_ability.html', pokemon_list=response.json()['pokemon_list'], ability_name=response.json()['ability_name'])
