#CSV
import csv
#with open("pokemones.csv") as pokemon:
#	pokebola=csv.reader(pokemon)
with open("pokemones.csv") as pokemon:
	pokebola=csv.DictReader(pokemon)

	for row in pokebola:
		print(row)


with open("pokemones.csv","w") as escribir:
	profesor_oak=csv.writer(escribir)
	profesor_oak.writerow(["bulbasur","planta","fuego"])
	

