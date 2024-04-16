import requests
import random

def get_pokemon():
    # Get user input for a Pokémon name
    pokemon_id = input("Enter a Pokémon name (in lowercase): ")

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")

    if response.status_code == 200:
        pokemon_data = response.json()
        print("Pokemon Name:", pokemon_data['name'])
        print("Pokemon ID:", pokemon_data['id'])
        return pokemon_data
    else:
        print("Error:", response.status_code)
        return None

def display_pokemon_info(pokemon):
    if pokemon:
        print("Name:", pokemon['name'])
        print("Abilities:", [ability['ability']['name'] for ability in pokemon['abilities']])
        print("Stats:")
        for stat in pokemon['stats']:
            print(stat['stat']['name'], ":", stat['base_stat'])
    else:
        print("No Pokemon data available.")

def battle(player_pokemon, cpu_pokemon):
    if player_pokemon and cpu_pokemon:
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
    else:
        print("Cannot start the battle. Pokemon data is missing.")

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
