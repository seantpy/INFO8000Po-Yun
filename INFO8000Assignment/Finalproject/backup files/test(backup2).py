from flask import Flask, render_template, request, jsonify, json
import sqlite3 as sql
import requests

app = Flask(__name__)



@app.route('/2')
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
 
@app.route('/')
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
    cur.execute("select * from forecast")
    rows2 = cur. fetchall();
    return render_template("data.html",rows = rows,rows2 =rows2)


@app.route('/forecast', methods=['POST'])
def forecast():
    
     if request.method == 'POST':
        try:
            City = request.form["City"]
            r= requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+City+'&appid=8f2980aea5484e2d60be6e013e5c0fda')
            json_object = r.json()
            d1dt_txt = json_object['list'][6]['dt_txt']
            d1tempk = json_object['list'][6]['main']['temp']
            d1main = json_object['list'][6]['weather'][0]['main']
            #we can replace "description" by "main"
            d2dt_txt = json_object['list'][14]['dt_txt']
            d2tempk = json_object['list'][14]['main']['temp']
            d2main = json_object['list'][14]['weather'][0]['main']
            d3dt_txt = json_object['list'][22]['dt_txt']
            d3tempk = json_object['list'][22]['main']['temp']
            d3main = json_object['list'][22]['weather'][0]['main']
            d4dt_txt = json_object['list'][30]['dt_txt']
            d4tempk = json_object['list'][30]['main']['temp']
            d4main = json_object['list'][30]['weather'][0]['main']
            d5dt_txt = json_object['list'][38]['dt_txt']
            d5tempk = json_object['list'][38]['main']['temp']
            d5main = json_object['list'][38]['weather'][0]['main']
            d1temp= (d1tempk - 273.15)*1.8+32
            d2temp= (d2tempk - 273.15)*1.8+32
            d3temp= (d3tempk - 273.15)*1.8+32
            d4temp= (d4tempk - 273.15)*1.8+32
            d5temp= (d5tempk - 273.15)*1.8+32
            msg1 = "day 1 time: " + str(d1dt_txt) + ", weather: " + str(d1main)+ ", temp: "+ str(d1temp)
            msg2 = "day 2 time: " + str(d2dt_txt) + ", weather: " + str(d2main)+ ", temp: "+ str(d2temp)
            msg3 = "day 3 time: " + str(d3dt_txt) + ", weather: " + str(d3main)+ ", temp: "+ str(d3temp)
            msg4 = "day 4 time: " + str(d4dt_txt) + ", weather: " + str(d4main)+ ", temp: "+ str(d4temp)
            msg5 = "day 5 time: " + str(d5dt_txt) + ", weather: " + str(d5main)+ ", temp: "+ str(d5temp)
            
            with sql.connect("GHdata.db") as con:
                
                con.execute ("""
                drop table if exists forecast
                """)
                
                con.execute ("""
                CREATE TABLE forecast (City,time,weather,temp);
                """)
                
                cur = con.cursor()
                cur.execute("INSERT INTO forecast (City,time,weather,temp) VALUES(?,?,?,?)",(City,d1dt_txt,d1main,d1temp))
                cur.execute("INSERT INTO forecast (City,time,weather,temp) VALUES(?,?,?,?)",(City,d2dt_txt,d2main,d2temp))
                cur.execute("INSERT INTO forecast (City,time,weather,temp) VALUES(?,?,?,?)",(City,d3dt_txt,d3main,d3temp))
                cur.execute("INSERT INTO forecast (City,time,weather,temp) VALUES(?,?,?,?)",(City,d4dt_txt,d4main,d4temp))
                cur.execute("INSERT INTO forecast (City,time,weather,temp) VALUES(?,?,?,?)",(City,d5dt_txt,d5main,d5temp))

                con.commit()
                msgrecord = "Record successfully added"
        
        except:
            con.rollback()
            msgrecord = "error in insert operation"
        
        finally:
            return render_template("WeatherResult.html",msgrecord=msgrecord, msg1 = msg1, msg2=msg2, msg3=msg3, msg4=msg4, msg5=msg5)
            con.close()
            


    
@app.route("/3")
def index():
    return render_template("weather.html")