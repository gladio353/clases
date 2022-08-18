from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql
from datetime import date
app=Flask(__name__)
@app.route("/")
def home():
	nombre="Federico Uprimny"
	con=sql.connect("db_web.db")
	con.row_factory=sql.Row
	cur=con.cursor()
	cur.execute("SELECT * FROM papers")
	data=cur.fetchall()
	print(data)
	return render_template("home.html",nombre=nombre,data=data)



@app.route("/add_paper", methods=["POST","GET"])
def add_paper():
	if request.method=="POST":
		titulo=request.form["titulo"]
		contenido=request.form["contenido"]
		fecha=date.today()
		con=sql.connect("db_web.db")
		cur=con.cursor()
		cur.execute("INSERT INTO papers(titulo,contenido,fecha) VALUES(?,?,?)",(titulo,contenido,fecha))
		con.commit()
		flash("papel agregado")
		return redirect(url_for("home"))


	return render_template("add_paper.html")

if __name__=="__main__":
	app.secret_key="1234"
	app.run(debug=True)
