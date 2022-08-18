import sqlite3 as sql
from datetime import date
conecion=sql.connect("db_web.db")
cursor=conecion.cursor()
cursor.execute("DROP TABLE IF EXISTS papers ")
cursor.execute("""CREATE TABLE "papers" (
"id" INTEGER PRIMARY KEY AUTOINCREMENT,
"titulo" TEXT,
"contenido" TEXT,
"fecha" TEXT
)""")
fecha=date.today()
fecha=str(fecha)
titulo="Frameworks"
contenido="Los Frameworks son estructuras de trabajo que te permiten crear applicativos en diversas tecnologias. Estoy aprendiendo a usar el Framework Flask de python para aplicaciones ligeras. Hasta el momento me ha parecido bastante util aunque al principio un pocon confuso pero cuando lo entiendes ya es mas facil."
cursor.execute("INSERT INTO papers(titulo,contenido,fecha) VALUES(?,?,?)",(titulo,contenido,fecha))
conecion.commit()
conecion.close()