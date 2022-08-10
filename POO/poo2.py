class Pokemon:
	def __init__(self,nombre,tipo):
		self.nombre=nombre
		self.tipo=tipo

	def ataque(self):
		if self.tipo=="fuego":
			print(self.nombre+"ataque llazallamaz")
		else:
			print("Wobafet")
pokemon= Pokemon("charizard","fuego")
print(pokemon.tipo)
print(pokemon.ataque())
pokemon2= Pokemon("lucario","lucha")
print(pokemon2.ataque())