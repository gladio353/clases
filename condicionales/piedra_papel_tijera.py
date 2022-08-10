#Piedra papel o tijera
from random import randint
opciones=["piedra","papel","tijera"]
a=False
while a==False:
	cpu=opciones[randint(0,2)]
	usuario=input("piedra,papel o tijera ? salir : ")

	if usuario==cpu:
		print("empate")
	elif usuario=="piedra":
		if cpu=="papel":
			print("Perdiste")
		else:
			print("Ganaste")
	elif usuario=="tijera":
		if cpu=="piedra":
			print("Perdiste")
		else:
			print("Ganaste")
	elif usuario=="papel":
		if cpu=="tijera":
			print("Perdiste")
		else:
			print("Ganaste")
	elif usuario=="salir":
		print("Gracias por jugar")
		a=True
	else:
		print("Error")
