from flask import Flask, render_template, request, jsonify, json
import sqlite3 as sql
import requests
import pandas as pd

app = Flask(__name__)



@app.route('/')
def home():
    return render_template ('homepage.html')
 
@app.route('/researcher')
def GreenHouse():
    return render_template ('GHDataImput.html')

@app.route('/farmer')
def farmer():
    return render_template ('FieldDataImput.html')



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
            con = sql.connect("GHdata.db")
            con.row_factory = sql.Row

            cur = con.cursor()
            cur.execute("select * from Greenhousedata")
            rows = cur.fetchall();
            
            return render_template("data.html",msg = msg,rows = rows)
            con.close()
            
            
@app. route('/data')
def data():
    con = sql.connect("GHdata.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from Greenhousedata")
    rows = cur.fetchall();
    return render_template("data.html",rows = rows)

@app. route('/data2')
def data2():
    con = sql.connect("GHdata.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from Greenhousedata")
    rows4 = cur.fetchall();
    return render_template("data2.html",rows4 = rows4)


@app.route('/farmerimput', methods=['POST', 'GET'])
def farmerimput():
    if request.method == 'POST':
        try:
            Field_Genotype = request.form['Field_Genotype']
            Lesion = request.form['Lesion']
            
            with sql.connect("GHdata.db") as con:
                cur = con.cursor()
                con.execute ("""
                drop table if exists fielddata
                """)
                
                con.execute ("""
                CREATE TABLE fielddata (Field_Genotype,Lesion);
                """)
                
                cur.execute("INSERT INTO fielddata (Field_Genotype,Lesion) VALUES(?,?)",(Field_Genotype,Lesion))
                
                con.commit()
                msgfield = "Field Record successfully added"
        
        except:
            con.rollback()
            msgfield = "error in insert operation"
        
        finally:
         
            con = sql.connect("GHdata.db")
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute("select * from fielddata")
            rows3 = cur. fetchall();
            return render_template("diseaseresult.html",msgfield=msgfield, rows3=rows3)
            con.close()
        
        
@app.route('/forecast', methods=['POST'])
def forecast():
    
     if request.method == 'POST':
        try:
            City = request.form["City"]
            r= requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+City+'&appid=8f2980aea5484e2d60be6e013e5c0fda')
            json_object = r.json()
            d1dt_txt = json_object['list'][6]['dt_txt']
            d1tempk = json_object['list'][6]['main']['temp_min']
            d1main = json_object['list'][6]['weather'][0]['main']
            #we can replace "description" by "main"
            d2dt_txt = json_object['list'][14]['dt_txt']
            d2tempk = json_object['list'][14]['main']['temp_min']
            d2main = json_object['list'][14]['weather'][0]['main']
            d3dt_txt = json_object['list'][22]['dt_txt']
            d3tempk = json_object['list'][22]['main']['temp_min']
            d3main = json_object['list'][22]['weather'][0]['main']
            d4dt_txt = json_object['list'][30]['dt_txt']
            d4tempk = json_object['list'][30]['main']['temp_min']
            d4main = json_object['list'][30]['weather'][0]['main']
            d5dt_txt = json_object['list'][38]['dt_txt']
            d5tempk = json_object['list'][38]['main']['temp_min']
            d5main = json_object['list'][38]['weather'][0]['main']
            d1temp= (d1tempk - 273.15)
            d2temp= (d2tempk - 273.15)
            d3temp= (d3tempk - 273.15)
            d4temp= (d4tempk - 273.15)
            d5temp= (d5tempk - 273.15)
            msg1 = "day 1 time: " + str(d1dt_txt) + ", weather: " + str(d1main)+ ", temp (min): "+ str(d1temp)
            msg2 = "day 2 time: " + str(d2dt_txt) + ", weather: " + str(d2main)+ ", temp (min): "+ str(d2temp)
            msg3 = "day 3 time: " + str(d3dt_txt) + ", weather: " + str(d3main)+ ", temp (min): "+ str(d3temp)
            msg4 = "day 4 time: " + str(d4dt_txt) + ", weather: " + str(d4main)+ ", temp (min):"+ str(d4temp)
            msg5 = "day 5 time: " + str(d5dt_txt) + ", weather: " + str(d5main)+ ", temp (min):"+ str(d5temp)
            
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
                
                msgrecord2 = "Record successfully added"
                cur.execute("select * from fielddata")
                data_field = pd.DataFrame(cur.fetchall(),columns = ['Field_Genotype','Lesion'])
                genotype = data_field.iloc[0,0]
                lesion = data_field.iloc[0,1]
                cur.execute("select * from forecast")
                data_temp = pd.DataFrame(cur.fetchall(),columns = ['City','time','weather','temp'])
                d1weather = data_temp.iloc[0,2]
                d2weather = data_temp.iloc[1,2]
                d3weather = data_temp.iloc[2,2]
                d4weather = data_temp.iloc[3,2]
                d5weather = data_temp.iloc[4,2]           
                d1temp = data_temp.iloc[0,3]
                d2temp = data_temp.iloc[1,3]
                d3temp = data_temp.iloc[2,3]
                d4temp = data_temp.iloc[3,3]
                d5temp = data_temp.iloc[4,3]
                if str(lesion) > "0.2":
                    if str(d1weather) == "Rain":
                        msgsug= "Chemical should be applied today"
                    elif str(d2weather) =="Rain":
                        msgsug= "Chemical should be applied tomorrow"
                    elif str(d3weather) =="Rain":
                        msgsug= "Chemical should be applied 2 days later"
                    elif str(d4weather) =="Rain":
                        msgsug= "Chemical should be applied 3 days later"
                    elif str(d5weather) =="Rain":
                        msgsug= "Chemical should be applied 4 days later"
                    elif d1temp > 24:
                        if str(genotype) == "628":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        elif str(genotype) == "660":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        elif str(genotype) == "668":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        elif str(genotype) == "708":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        else:
                            msgsug= "Symptom of disease is observered, but it won't rain this week. Chemical is not neccessary."
                    elif d2temp > 24:
                        if str(genotype) == "628":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        elif str(genotype) == "660":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        elif str(genotype) == "668":
                            msgsug= "SSymptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        elif str(genotype) == "708":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        else:
                            msgsug= "Symptom of disease is observered, but it won't rain this week. Chemical is not neccessary."
                    elif d3temp > 24:
                        if str(genotype) == "628":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        elif str(genotype) == "660":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        elif str(genotype) == "668":
                            msgsug= "SSymptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        elif str(genotype) == "708":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        else:
                            msgsug= "Symptom of disease is observered, but it won't rain this week. Chemical is not neccessary."
                    elif d4temp > 24:
                        if str(genotype) == "628":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        elif str(genotype) == "660":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        elif str(genotype) == "668":
                            msgsug= "SSymptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        elif str(genotype) == "708":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chemical should be applied today. "
                        else:
                            msgsug= "Symptom of disease is observered, but it won't rain this week. Chemical is not neccessary."
                    elif d5temp > 24:
                        if str(genotype) == "628":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chenical should be applied today. "
                        elif str(genotype) == "660":
                            msgsug= "test Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chenical should be applied today. "
                        elif str(genotype) == "668":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chenical should be applied today. "
                        elif str(genotype) == "708":
                            msgsug= "Symptom of disease is observered. Though it won't rain this week, the genotype of peanut is vulnerable. Chenical should be applied today. "
                        else:
                            msgsug= "Symptom of disease is observered, but it won't rain this week. Chemical is not neccessary"
                    else: 
                        msgsug= "Symptom of disease is observered, but it won't rain this week. Considring temperature is lower than 24'C, chemical is not neccessary, no matter what genotype of peanut it is. "
                else: 
                    msgsug= "Symptom of disease is not significant. Chemical is not neccessary so far."     
            
        except:
            con.rollback()
            msgrecord2 = "error in insert operation"
        
        finally:
            con = sql.connect("GHdata.db")
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute("select * from forecast")
            rows2 = cur. fetchall();
            cur.execute("select * from fielddata")
            rows5 = cur. fetchall();
            
            return render_template("WeatherResult.html",msgrecord2=msgrecord2,rows2 =rows2,rows5=rows5,msgsug=msgsug)
            
            #return render_template("WeatherResult(backup).html",msgrecord2=msgrecord2, msg1 = msg1, msg2=msg2, msg3=msg3, msg4=msg4, msg5=msg5, msgsug=msgsug)
            
            con.close()
            
            
@app.route('/suggestion')
def suggestion():
    con = sql.connect("GHdata.db")
    cur = con.cursor()
    cur.execute("select * from forecast")
    #change city manually

    r= requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+'taipei'+'&appid=8f2980aea5484e2d60be6e013e5c0fda')
    json_object = r.json()
    d1main = json_object['list'][6]['weather'][0]['main']
    d2main = json_object['list'][14]['weather'][0]['main']
    d3main = json_object['list'][22]['weather'][0]['main']
    d4main = json_object['list'][30]['weather'][0]['main']
    d5main = json_object['list'][38]['weather'][0]['main']
    
    if d1main == "Rain":
        msgsuc= "Chemical Application today"
        return render_template("Suggestion.html",msg_suggestion=msgsuc)
    elif d2main == "Rain":
        msgsuc= "Chemical Application tomorrow"
        return render_template("Suggestion.html",msg_suggestion=msgsuc)
    elif d3main == "Rain":
        msgsuc= "Chemical Application two days later"
        return render_template("Suggestion.html",msg_suggestion=msgsuc)
    elif d4main == "Rain":     
        msgsuc= "Chemical Application three days later"
        return render_template("Suggestion.html",msg_suggestion=msgsuc)
    elif d5main == "Rain":
        msgsuc= "Chemical Application four days later"
        return render_template("Suggestion.html",msg_suggestion=msgsuc)
    else:    
        msgfail= "Chemical should not be applied"
        return render_template("Suggestion.html",msg_suggestion=msgfail)

            


    
@app.route("/3")
def index():
    return render_template("weather.html")

@app.route("/test")
def test():
    con = sql.connect("GHdata.db")        
    cur = con.cursor()  
    cur.execute("select * from fielddata")
    
    data_field = pd.DataFrame(cur.fetchall(),columns = ['Field_Genotype','Lesion'])
    genotype = data_field.iloc[0,0]
    lesion = data_field.iloc[0,1]
    
    cur.execute("select * from forecast")
    data_field = pd.DataFrame(cur.fetchall(),columns = ['City','time','weather','temp'])
    d1weather = data_field.iloc[0,2]
    d2weather = data_field.iloc[1,2]
    d3weather = data_field.iloc[2,2]
    d4weather = data_field.iloc[3,2]
    d5weather = data_field.iloc[4,2]           
    
   