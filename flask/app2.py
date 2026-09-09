from flask import Flask,render_template,request
import mysql.connector
import os

obj=Flask(__name__)
def h():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.environ.get("MYPASSWORD"),
        database="col"
    )

@obj.route("/")
def t():
    return render_template("index.html")

@obj.route("/submit",methods=["POST"])
def m():
   data=request.form["data"]
   l=h()
   cursor=l.cursor()
   sql="insert into html (data) values(%s)"
   cursor.execute(sql,(data,))
   l.commit
   cursor.close
   l.close
   return "flask worked"

if __name__ == "__main__":
    obj.run(debug=True)