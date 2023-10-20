from flask import request, jsonify, Blueprint
from auth import verify_token, get_users
import requests

pokemon_app = Blueprint('pokemon', __name__)

@pokemon_app.route('/api/pokemon/<nome_pokemon>', methods=['GET'])
def get_pokemon(nome_pokemon):
    token = request.headers.get('Authorization')
    if not token:
        return 'Token não fornecido', 401

    users = get_users()
    data_load = verify_token(token)

    if not data_load or 'user' not in data_load:
        return 'Insira um token válido', 401

    user_token = data_load['user']

    for user_info in users:
        if 'user' in user_info and user_info['user'] == user_token:
            poke_url = f'https://pokeapi.co/api/v2/pokemon/{nome_pokemon}'
            response = requests.get(poke_url)
            data = response.json()

    result_data = {
        'forms': data['forms'],
        'moves': data['moves']
    }

    return jsonify(result_data)
