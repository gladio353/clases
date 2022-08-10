#Abrir archivo
pokemones = open("pokemones.txt","r")
print(pokemones.read())
pokemones.close()

#Agregar dato
pokemones= open("pokemones.txt","a")
pokemones.write("Charizard")
pokemones.close()

#Transcribir
pokemones=open("pokemones.txt","w")
pokemones.write("Mi nueva POkedex")
pokemones.close()

#Creacion de archivo
#archivo=open("nuevo.txt","x") 
#archivo.write("Mi nuevo archivo")
#archivo.close()

#Borrar archivo
import os 
os.remove("nuevo.txt")
