import pandas
pokedex={
	"pokemones":["pikachu","lucario","charmander"],
	"tipos":["electrico","lucha","fuego"]}

data=pandas.DataFrame(pokedex)
print(data)
print(data.loc[2])
