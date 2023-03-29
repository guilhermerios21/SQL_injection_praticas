import os
from flask import Flask
from flask import Markup
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy import create_engine

#db_connect = create_engine('mysql://root:my-password@db/my_database')
db_connect = create_engine('sqlite:///mydb.db')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_connect

@app.route("/login")
def teste():
    # Recuperar parâmetros passados via URL após "?"
    id = request.args.get('id')
    user = request.args.get('user')
    password = request.args.get('password')
    
    sql_Query_Injection = text("select * from user where id={}".format(id))
    sql_Query_Not_Injection = text("select * from user where id=:user_id")

    conn = db_connect.connect()
    result = conn.execute(sql_Query_Not_Injection, user_id = id)

    # user = [row[1] for row in result]
    content = "<table>"
    content = content + str("<tr>")
    content = content + str("<th>id</th>")
    content = content + str("<th>user</th>")
    content = content + str("<th>password</th>")
    content = content + str("</tr>")

    for row in result:
        content = content + str("<tr>")
        content = content + str("<td>"+str(row[0])+"</td>")
        content = content + str("<td>"+str(row[1])+"</td>")
        content = content + str("<td>"+str(row[2])+"</td>")
        content = content + str("</tr>")
        

    content = content + str("</table>")
    # print(content)
    result = Markup(content)

    return render_template('index.html', result=result)
    

if __name__ == "__main__":
    app.run(debug=True)