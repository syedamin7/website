from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


def get_database():

    connection = sqlite3.connect("database.db")

    connection.row_factory = sqlite3.Row

    return connection


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/api/hospitals")
def hospitals():

    name = request.args.get("name", "")

    db = get_database()

    hospitals = db.execute(
        """
        SELECT * FROM hospitals
        WHERE name LIKE ?
        """,
        ("%" + name + "%",)
    ).fetchall()

    db.close()

    return jsonify([dict(row) for row in hospitals])


@app.route("/api/pharmacies")
def pharmacies():

    db = get_database()

    pharmacies = db.execute(
        "SELECT * FROM pharmacies"
    ).fetchall()

    db.close()

    return jsonify([dict(row) for row in pharmacies])


@app.route("/api/blood")
def blood():

    group = request.args.get("group", "")

    db = get_database()

    donors = db.execute(
        """
        SELECT * FROM blood
        WHERE blood_group = ?
        """,
        (group,)
    ).fetchall()

    db.close()

    return jsonify([dict(row) for row in donors])


if __name__ == "__main__":
    app.run(debug=True)


    