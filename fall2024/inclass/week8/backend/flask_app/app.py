from flask import Flask, render_template, send_from_directory, jsonify
from flask_cors import CORS
from .model import PokeClient
app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
poke_client = PokeClient()

CORS(app, supports_credentials=True)


# We will run the backend in one terminal and the frontend in another terminal
"=============**************API CODE**************==================="    
# Gets the list of pokemon and returns 200
@app.route('/get_pokemon_list', methods=['GET'])
def get_pokemon_list():
    return jsonify({
        "pokemon_list": poke_client.get_pokemon_list(),
        "pokemon_ids": poke_client.get_pokemon_ids()
        }), 200


# Gets poke info and returns 200 if successful, 500 if not
@app.route('/get_pokemon_info/<pokemon_name>', methods=['GET'])
def get_pokemon_info(pokemon_name):
    try:
       return jsonify({
            'info': poke_client.get_pokemon_info(pokemon_name),
            'pokemon_name': pokemon_name
        }), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
    
# Gets the list of pokemon with the ability and returns 200 if successful, 500 if not
@app.route('/get_pokemon_with_ability/<ability_name>')
def get_pokemon_with_ability(ability_name):
    try:
        return jsonify({
                'pokemon_list': poke_client.get_pokemon_with_ability(ability_name),
                'ability_name': ability_name
            }), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
    



"=============**************OLD CODE**************==================="    
@app.route('/')
def index():
    """
    Must show all of the pokemon names as clickable links

    Check the README for more detail.
    """
    
    return render_template('index.html',
                           pokemon_list=poke_client.get_pokemon_list(),poke_ids=poke_client.get_pokemon_ids())

@app.route('/pokemon/<pokemon_name>')
def pokemon_info(pokemon_name):
    """
    Must show all the info for a pokemon identified by name

    Check the README for more detail
    """
    return render_template('pokemon_info.html',
                           pokemon_name=pokemon_name,
                           info=poke_client.get_pokemon_info(pokemon_name))

@app.route('/ability/<ability_name>')
def pokemon_with_ability(ability_name):
    """
    Must show a list of pokemon 

    Check the README for more detail
    """
    return render_template('pokemon_with_ability.html',
                           ability_name=ability_name,
                           pokemon_list=poke_client.get_pokemon_with_ability(ability_name))
