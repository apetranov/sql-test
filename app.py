import sqlite3
import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__, static_folder="images")

def get_db_connection():
    conn = sqlite3.connect("people.db")
    conn.row_factory = sqlite3.Row  # Allows you to access columns by name
    return conn


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if not request.form.get("first_name"):
            return render_template("error1.html")
        elif not request.form.get("last_name"):
            return render_template("error2.html")
        elif not request.form.get("email"):
            return render_template("error3.html")
        
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO people (first_name, last_name, email) VALUES (?, ?, ?)", (first_name, last_name, email))
        conn.commit()
        conn.close()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM people")
    people = cursor.fetchall()
    conn.close()

    people_info = []
    for person in people:
        person_info = dict(person)
        people_info.append(person_info)

    return render_template("index.html", people=people_info)