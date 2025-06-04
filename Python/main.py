import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '171d26c4841d3378f295f60c98100cda'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Karim",
    "photo_id": 35
}
body_chenge = {
    "pokemon_id": "330931",
    "name": "Tim",
    "photo_id": 10
}
body_pokeball = {
    "pokemon_id": "330931"
}

'''response_create = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_chenge = requests.put(url = f'{URL}/pokemons' , headers = HEADER, json = body_chenge)
print(response_chenge.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER, json = body_pokeball)
print(response_pokeball.text)

