import requests
import json
import random

# poke_req = requests.get("https://pokeapi.co/api/v2/pokemon/empoleon")
# # print(poke_req.json())
#
# poke_data = json.loads(poke_req.text)
# print(type(poke_data))

# print(poke_data["name"])
# print(poke_data["height"])

# Get user input for a Pokémon name
player_pokemon_name = input("Enter a Pokémon name (in lowercase): ")

# Send a GET request to the API
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{player_pokemon_name}")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Display the response data
    pokemon_data = response.json()
    print("Pokemon Name:", pokemon_data['name'])
    print("Pokemon ID:", pokemon_data['id'])

else:
    # If the request was not successful, print an error message
    print("Error:", response.status_code)

def battle(player_pokemon, cpu_pokemon):
    player_hp = player_pokemon['stats'][0]['base_stat']
    cpu_hp = cpu_pokemon['stats'][0]['base_stat']
    while player_hp > 0 and cpu_hp > 0:
        player_attack = random.randint(1, 10)
        cpu_attack = random.randint(1, 10)
        player_hp -= cpu_attack
        cpu_hp -= player_attack
        print("Player HP:", player_hp)
        print("CPU HP:", cpu_hp)

# def get_random_pokemon():
#     # gets random pokemon
#     return random.randint(1, 15)

# def player_choose_pokemon():

    # lets the player choose a pokemon from 0 to 15

#
# def allocate_pokemon():
#     # assigns a Pokémon to the opponent using getRandomPokemon
#     opponent_id = get_random_pokemon()
#     return opponent_id