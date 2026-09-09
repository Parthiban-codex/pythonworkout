from flask import Flask,render_template,request
import sql.connector
import os

obj=Flask(__name__)
def h():
    return sql.connector.connect(
        host="localhost",
        user="root"
        password=os.environ.get("MYPASSWORD"),
        database="col"
    )

@obj.route("/")
def t():
    return render_template("index.html")

@obj.route("/submit",method=["POST"])
def m():
   