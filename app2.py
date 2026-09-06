from flask import Flask, render_template, request
import mysql.connector 
app=Flask(__name__)
def dba():
    return mysql.connector.connect(
    host ="localhost",
    user="root",
    password="parthiban",
    database="x")

@app.route("/")    
def h():
    return render_template("iform.html")

@app.route("/submit" , methods=["post"])  
def s():
    data=request.form["data"]  
    db=dba()
    cursor = db.cursor()
    sql="insert into xx (data) values(%s)"
    cursor.execute(sql,(data,))
    db.commit()
    cursor.close()
    db.close()
    return "saved go and check db"
    
if __name__ == "__main__":
    app.run(debug=True)


