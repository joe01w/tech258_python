import requests
import random


def get_pokemon():
    pokemon_id = random.randint(1, 1025)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve Pokémon data.")


def display_pokemon_info(pokemon):
    print("Name:", pokemon['name'])
    print("Abilities:", [ability['ability']['name'] for ability in pokemon['abilities']])
    print("Stats:")
    for stat in pokemon['stats']:
        print(stat['stat']['name'], ":", stat['base_stat'])


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

    if player_hp <= 0 and cpu_hp <= 0:
        print("It's a draw!")
    elif player_hp <= 0:
        print(f"{cpu_pokemon['name']} wins!")
    else:
        print(f"{player_pokemon['name']} wins!")


def main():
    player_pokemon = get_pokemon()
    cpu_pokemon = get_pokemon()

    print("Your Pokémon:")
    display_pokemon_info(player_pokemon)
    print("\nCPU's Pokémon:")
    display_pokemon_info(cpu_pokemon)

    print("\nLet the battle begin!")
    battle(player_pokemon, cpu_pokemon)


if __name__ == "__main__":
    main()
