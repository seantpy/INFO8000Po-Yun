from flask import Flask, render_template, request, jsonify, json
import sqlite3 as sql


app = Flask(__name__)



@app.route('/')
def home():
    return """<p> INFO8000 FINAL PROJECT</p>
            <p>Po-Yun Teng and Yun-Ching Tsai</p>
            <p>Instruction </p>
            <p> /newdata : enter new data </p>   
            <p> /data  : read dataset</p>
            <p> This tool is developed to advice peanut researchers or farmers on chemical application program for stem rot disease management in field based on weather forecast. Disease progress will be estimated by instant field disease situation.</p>
            <p>Data description:  Each data collection includes 7 variables</p>
            <p>GenotypeNumber: a specific number assigned to genotype</p>
            <p>Genotype: full name of peanut genotype.</p> 
            <p>rep: indicate replication number</p>
            <p>DAI3: lesion length recorded at 3 days after stem rot disease occurrence</p>
            <p>DAI5: lesion length recorded at 5 days after stem rot disease occurrence</p> 
            <p> DAI7: lesion length recorded at 7 days after stem rot disease occurrence</p>
            <p>DAI9: lesion length recorded at 9 days after stem rot disease occurrence</p>"""
 
@app.route('/newdata')
def GreenHouse():
    return render_template ('DataImput.html')



@app.route('/addrec2', methods = ['POST', 'GET'])
def addrec2():
    if request.method == 'POST':
        try:
            GenotypeNumber = request.form['GenotypeNumber']
            Genotype = request.form['Genotype']
            rep = request.form['rep']
            DAI3 = request.form['DAI3']
            DAI5 = request.form['DAI5']
            DAI7 = request.form['DAI7']
            DAI9 = request.form['DAI9']
            
            with sql.connect("GHdata.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Greenhousedata (GenotypeNumber,Genotype,rep,DAI3,DAI5,DAI7,DAI9) VALUES(?,?,?,?,?,?,?)",(GenotypeNumber,Genotype,rep,DAI3,DAI5,DAI7,DAI9))
                
                con.commit()
                msg = "Record successfully added"
        
        except:
            con.rollback()
            msg = "error in insert operation"
        
        finally:
            return render_template("result.html",msg = msg)
            con.close()
            


@app. route('/data')
def data():
    con = sql.connect("GHdata.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from Greenhousedata")
    rows = cur.fetchall();
    return render_template("data.html",rows = rows)
