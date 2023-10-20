from flask import request, jsonify, Blueprint
from jwt.exceptions import DecodeError
import json
import jwt

auth_app = Blueprint('auth', __name__)

APP_KEY = 'pokemon'

def generate_token(user):
    data_load = {'user': user}
    return jwt.encode(data_load, APP_KEY, algorithm='HS256')

def get_users():
    with open('users.json', 'r') as users_file:
        users = json.load(users_file)
    return users

@auth_app.route('/api/auth', methods=['POST'])
def authenticate():
    data = request.get_json()
    users = get_users()

    for user_info in users:
        if user_info['user'] == data['user'] and user_info['password'] == data['password']:
            token = generate_token(data['user'])
            return jsonify({'token': token})
        
    return 'Nome do usuário ou senha incorreto', 401

def verify_token(token):
    try:
        data_load = jwt.decode(token, APP_KEY, algorithms=['HS256'])
        return data_load
    except DecodeError:
        return None
