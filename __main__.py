from flask import Flask, render_template
import sqlite3
import os

# create a new flask app
app = Flask(__name__)

# create a function that will be called when the user accesses the root of the website
def get_db_connection():
    dir = os.getcwd() + '/patients.db'
    print('dir:', dir)
    conn = sqlite3.connect(dir)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    db = get_db_connection()
    patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
    db.close()
    print('patientListSql:', patientListSql)
    return render_template('index.html', listPatients=patientListSql) 

@app.route('/bootstrap')
def bootstrap():
    conn = get_db_connection()
    patientListSql = conn.execute('SELECT * FROM patient_table').fetchall()
    conn.close()
    print('patientListSql:', patientListSql)
    return render_template('bootstrap_example.html', listPatients=patientListSql)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
