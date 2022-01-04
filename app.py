import os
from flask import Flask, render_template, request, flash, redirect
import sqlite3

from flask.helpers import url_for

if not os.path.exists('img_db.db'):
    connection = sqlite3.connect('img_db.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())
    cur = connection.cursor()
    connection.commit()
    connection.close()

def get_connection():
    connection = sqlite3.connect('img_db.db')
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        imgname = request.form['imgname']
        imgurl = request.form['imgurl']
        imgdetails = request.form['imgdetails']
        if not imgname or not imgurl or not imgdetails:
            flash("All Details are required!")
        else:
            connection = get_connection()
            connection.execute('INSERT INTO images (imgname, imgurl, imgdetails) VALUES(?, ?, ?)', (imgname, imgurl, imgdetails))
            connection.commit()
            connection.close()
            flash("Image submitted Successfully!")
        return redirect('/')
    
    connection = get_connection()
    images = connection.execute('SELECT * FROM images').fetchall()
    connection.close()
    return render_template("index.html", images=images)

@app.route("/show/<int:id>")
def show(id):
    connection = get_connection()
    image = connection.execute('SELECT * FROM images WHERE id=?', (id,)).fetchone()
    connection.close()
    if bool(image):
        return render_template("show_image.html", image=image)
    flash("No Image with this ID Found!")
    return redirect("/")

@app.route("/new")
def add_new():
    return render_template("new.html")

@app.route("/<int:id>/edit", methods=["GET", "PUT"])
def edit(id):
    if request.method == "PUT":
        imgname = request.form['imgname']
        imgurl = request.form['imgurl']
        imgdetails = request.form['imgdetails']
        if not imgname or not imgurl or not imgdetails:
            flash("All Details are required!")
        else:
            connection = get_connection()
            connection.execute('UPDATE images SET imgname = ?, imgurl = ?, imgdetails = ? WHERE id = ?', (imgname, imgurl, imgdetails, id))
            connection.commit()
            connection.close()
            flash("Image Updated Successfully!")
        return "Image Updated Successfully!"
    
    connection = get_connection()
    image = connection.execute('SELECT * FROM images WHERE id=?', (id,)).fetchone()
    connection.close()
    if bool(image):
        return render_template("edit.html", image=image)
    flash("No Image with this ID Found!")
    return redirect('/')

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    if request.method == "DELETE":
        connection = get_connection()
        image = connection.execute('SELECT * FROM images WHERE id=?', (id,)).fetchone()
        connection.close()
        if bool(image):
            connection = get_connection()
            connection.execute('DELETE FROM images WHERE id = ?', (id,))
            connection.commit()
            connection.close()
            flash(f"Image Deleted Successfully!")
            return "Image Deleted Successfully!"
        flash("No Image with this ID Found!")
        return "No Image with this ID Found!"
    return redirect('/')