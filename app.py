from flask import Flask, render_template
import mysql.connector
#from birdseye import eye

app = Flask(__name__)

#@eye
@app.route("/")
# def hello():
#     return 'Hello, World!'
def my_sql():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="yourdb"
    )
    cursor = connection.cursor()


    query = "SELECT * FROM employee"
    cursor.execute(query)
    data = cursor.fetchall()


    connection.close()

   
    return render_template('mysqldata.html', data=data)



if __name__ == '__main__':
    app.run()