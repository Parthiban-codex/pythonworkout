from flask import Flask, render_template_string, request
import os
import mysql.connector
app=Flask(__name__)
def p():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.environ.get("MYPASSWORD"),
        database="col"
    )
html="""
<html>
<body>
  <table>
          <form action="/submit" method="POST">
    
        <tr>
        
            <td>
               DATA: 
                </td>
                <td><input type="text" name="name" Placeholder="Enter the name" required></td>
                <td><button>Submit</button></td>
            </tr>
            </form>
    </table>

</body></html>
"""
@app.route("/")
def home():
    return render_template_string(html)
@app.route("/submit",methods=["POST"])    
def home2():
    name=request.form["name"]
    obj=p()
    cursor=obj.cursor()
    
    sql="insert into p (name) values(%s)"
    cursor.execute(sql,(name,))
    obj.commit()
    cursor.close()
    obj.close()
    return "saved..."

if __name__ == "__main__":
    app.run(debug=True)