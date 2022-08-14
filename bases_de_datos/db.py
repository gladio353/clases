import sqlite3

conecion= sqlite3.connect("pokemones.db")
cursor= conecion.cursor()

#comando para crear tabla
#cursor.execute("""CREATE TABLE "pokemones"(
#"id" INTEGER PRIMARY KEY AUTOINCREMENT,
#"nombre" VARCHAR,
#"tipo" VARCHAR,
#"nivel" INTEGER);""")

#comando para insertar dato
#cursor.execute("""INSERT INTO pokemones ("nombre","tipo","nivel") VALUES ("pikachu","electrico",39); """)

#comando para editar dato
#cursor.execute("""UPDATE pokemones SET nivel=40 WHERE nombre="pikachu";""")

cursor.execute("""DELETE FROM pokemones WHERE "id"=2;""")
cursor.execute("""SELECT * FROM pokemones;""")
print(cursor.fetchall())
conecion.commit()
conecion.close()