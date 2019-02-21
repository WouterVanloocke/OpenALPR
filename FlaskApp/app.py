from flask import Flask, request, render_template
from flask_socketio import SocketIO
import pymysql
import subprocess
from subprocess import Popen, PIPE

#from flaskext.mysql import MySQL
db = pymysql.connect("localhost", "root", "plate", "plates")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
subprocess.Popen("/home/wouter/filmpje.py", shell=True)
process = Popen(['python', 'filmpje.py'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout)

# mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'plate'
# app.config['MYSQL_DATABASE_DB'] = 'plates'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

# conn = mysql.connect()
# cursor =conn.cursor()

# cursor.execute("SELECT * from medewerkers")
# data = cursor.fetchone()

@app.route('/')
def someName():
    cursor = db.cursor()
    sql = "SELECT nummerplaat FROM plaat"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results=results)

    # for line in results:
    #     if line == x:
    #         sql = "SELECT medewerkers.voornaam AS voornaam, medewerkers.achternaam AS achternaam  FROM medewerkers INNER JOIN plaat ON medewerkers.id = plaat.eigenaar_id AND medewerkers.id "
    #         cursor.execute(sql)
    #         resultaten = cursor.fetchall()
    #         return render_template('index.html', results=resultaten)
    #     if not line == x:
    #         pass

if __name__ == '__main__':
   socketio.run(app)
