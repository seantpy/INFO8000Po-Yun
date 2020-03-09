from flask import Flask, render_template, request, jsonify, json
import sqlite3 as sql


app = Flask(__name__)



@app.route('/')
def home():
    return "HI INFO8000 TEST! Here is the instruction ; /entervaccine  : enter new data  ;   /list  : read dataset"
 
@app.route('/entervaccine')
def vaccine():
    return render_template ('vaccine.html')



@app.route('/addrec2', methods = ['POST', 'GET'])
def addrec2():
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
