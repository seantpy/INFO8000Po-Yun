from flask import Flask, render_template, request, jsonify, json
import sqlite3 as sql


app = Flask(__name__)



@app.route('/')
def home():
    return "HI INFO8000 TEST! Here is the instruction ; /entervaccine  : enter new data  ;   /list  : read dataset"
 
@app.route('/entervaccine')
def vaccine():
    return render_template ('vaccine.html')


<<<<<<< HEAD
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
=======

@app.route('/addrec2', methods = ['POST', 'GET'])
def addrec2():
>>>>>>> 2f57c932c7bf6891d391a5424dee6f5913e2cacc
    if request.method == 'POST':
        try:
            trademark = request.form['trademark']
            manufacturer = request.form['manufacturer']
            types = request.form['types']
            species = request.form['species']
            
            with sql.connect("database2.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO vaccines2 (trademark,manufacturer,types,species) VALUES(?,?,?,?)",(trademark,manufacturer,types,species))
                
                con.commit()
                msg = "Record successfully added"
        
        except:
            con.rollback()
            msg = "error in insert operation"
        
        finally:
            return render_template("results.html",msg = msg)
            con.close()
            


@app. route('/list')
def list():
    con = sql.connect("database2.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from vaccines2")
    rows = cur.fetchall();
    return render_template("list.html",rows = rows)
<<<<<<< HEAD
    
@app. route('/lists')
def list2():
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    records = connection.execute("SELECT NAME from students")
    return jsonify(records)
=======
>>>>>>> 2f57c932c7bf6891d391a5424dee6f5913e2cacc
