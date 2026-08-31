from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",              
        database="college_db"
    )


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]

    db = get_db_connection()
    cursor = db.cursor()

    sql = "INSERT INTO students (name, email) VALUES (%s, %s)"

    cursor.execute(sql, (name, email))

    db.commit()

    cursor.close()
    db.close()

    return "Student saved successfully!"


if __name__ == "__main__":
    app.run(debug=True)
