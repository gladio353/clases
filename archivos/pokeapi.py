#API
import requests
charizard=requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
print(charizard.json()["name"])
