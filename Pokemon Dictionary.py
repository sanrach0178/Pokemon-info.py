import requests

while True:

    pokemon=input("Enter the name of the pokemon: ")

    poke_url=f"https://pokeapi.co/api/v2/pokemon/{pokemon}"


    data=requests.get(poke_url)

    try:
        
        data2=data.json()
        print(f"Name: {data2['name'].capitalize()}")
        print(f"ID: {data2['id']}")
        types = [t['type']['name'] for t in data2['types']]
        print(f"Types: {', '.join(types)}")

        print(f"Height: {data2['height']*10}cm")
        print(f"Weight: {data2['weight']/10}kg")

        abilities = [a ['ability']['name'] for a in data2['abilities']]
        print(f"Abilities: {', '.join(abilities)}")

    except:
        print("Invalid Pokemon name. Please check the spelling and try again.")




    