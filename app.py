from flask import Flask
from auth import auth_app
from pokemon import pokemon_app
from ability import ability_app

app = Flask(__name__)

app.register_blueprint(auth_app)
app.register_blueprint(pokemon_app)
app.register_blueprint(ability_app)

if __name__ == "__main__":
    app.run(debug=True)
