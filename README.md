# API do Pokémon com Flask
Este é um aplicativo em Flask que fornece autenticação e permite acessar dados da 
[PokeAPI](https://pokeapi.co/). A aplicação gera um token JWT para autenticação e 
permite fazer solicitações à PokeAPI com acesso autorizado. 

## Funcionamento
A aplicação tem três principais funcionalidades:

1. **Autenticação:** Através do endpoint `/api/auth`, você pode gerar um token JWT para autenticação que é necessário para acessar as outras funcionalidades.

2. **Obter Dados do Pokémon:** O endpoint `/api/pokemon/<nome_pokemon>` permite acessar informações 
sobre um Pokémon específico na PokeAPI.

3. **Obter Dados de Habilidade:** O endpoint `/api/habilidade/<nome_pokemon>` acessar informações sobre a habilidade de um Pokémon.

## Como Executar
1. **Clonar o Repositório:** Clone este repositório em sua máquina local usando `git clone`.

2. **Instalar Dependências:** Instale as dependências necessárias executando o seguinte comando:

`pip install -r requirements.txt`

3. **Executar o Aplicativo:** Execute o aplicativo Flask com o seguinte comando:

`python app.py`

O aplicativo será iniciado e estará disponível em `http://127.0.0.1:5000/`.

## Dependências
- Flask: Um microframework da web para Python.
- Requests: Usado para fazer solicitações HTTP à PokeAPI.
- PyJWT: Uma biblioteca Python para Tokens JSON Web.
