
from flask import Flask, render_template, request, jsonify, json
import sqlite3 as sql
import requests
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
from io import BytesIO
import base64
import statsmodels.api as sm

import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

def getCurrFigAsBase64HTML():
    im_buf_arr = BytesIO()
    plt.gcf().savefig(im_buf_arr,format='png')
    im_buf_arr.seek(0)
    b64data = base64.b64encode(im_buf_arr.read()).decode('utf8');
    return render_template('img.html',img_data=b64data) 

def getCurrFigAsBase64HTML2():
    im_buf_arr = BytesIO()
    plt.gcf().savefig(im_buf_arr,format='png')
    im_buf_arr.seek(0)
    b64data = base64.b64encode(im_buf_arr.read()).decode('utf8');
    return render_template('img2.html',img_data=b64data) 
def getCurrFigAsBase64HTML3():
    im_buf_arr = BytesIO()
    plt.gcf().savefig(im_buf_arr,format='png')
    im_buf_arr.seek(0)
    b64data = base64.b64encode(im_buf_arr.read()).decode('utf8');
    return render_template('img3.html',img_data=b64data) 
def getCurrFigAsBase64HTML4():
    im_buf_arr = BytesIO()
    plt.gcf().savefig(im_buf_arr,format='png')
    im_buf_arr.seek(0)
    b64data = base64.b64encode(im_buf_arr.read()).decode('utf8');
    return render_template('img4.html',img_data=b64data) 

def getCurrFigAsBase64HTML5():
    im_buf_arr = BytesIO()
    plt.gcf().savefig(im_buf_arr,format='png')
    im_buf_arr.seek(0)
    b64data = base64.b64encode(im_buf_arr.read()).decode('utf8');
    return render_template('img5.html',img_data=b64data) 

def getCurrFigAsBase64HTML6():
    im_buf_arr = BytesIO()
    plt.gcf().savefig(im_buf_arr,format='png')
    im_buf_arr.seek(0)
    b64data6 = base64.b64encode(im_buf_arr.read()).decode('utf8');
    return render_template('img6.html',img_data6=b64data6)

def getCurrFigAsBase64HTML7():
    im_buf_arr = BytesIO()
    plt.gcf().savefig(im_buf_arr,format='png')
    im_buf_arr.seek(0)
    b64data = base64.b64encode(im_buf_arr.read()).decode('utf8');
    return render_template('img7.html',img_data=b64data) 

def getCurrFigAsBase64HTML8():
    im_buf_arr = BytesIO()
    plt.gcf().savefig(im_buf_arr,format='png')
    im_buf_arr.seek(0)
    b64data = base64.b64encode(im_buf_arr.read()).decode('utf8');
    return render_template('img8.html',img_data=b64data) 



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
            GenotypeNumber = request.form['GenotypeNumber'] or None
            Genotype = request.form['Genotype']
            rep = request.form['rep'] or None
            exp = request.form['exp'] or None
            DAI3 = request.form['DAI3'] or None
            DAI5 = request.form['DAI5'] or None
            DAI7 = request.form['DAI7'] or None
            DAI9 = request.form['DAI9'] or None
            
            
            with sql.connect("GHdata.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Greenhousedata (GenotypeNumber,Genotype,rep,exp, DAI3,DAI5,DAI7,DAI9) VALUES(?,?,?,?,?,?,?,?)",(GenotypeNumber,Genotype,rep,exp,DAI3,DAI5,DAI7,DAI9))
                
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
            
@app. route('/data2')
def data2():
    con = sql.connect("GHdata.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from Greenhousedata")
    rows4 = cur.fetchall();
    
    
        
    return render_template("data2.html",rows4 = rows4)
 

            
@app. route('/figure')
def figure():
    
    conn = sql.connect("GHdata.db")
    cursor = conn.execute("select * from Greenhousedata")
    c= conn.cursor()
    df1 = pd.DataFrame(cursor.fetchall(),columns = ['GenotypeNumber','Genotype','rep','exp','DAI3','DAI5','DAI7','DAI9'], dtype=float) 
    convert_dict = {'GenotypeNumber': str, 'Genotype':  str,} 
    df = df1.astype(convert_dict) 
    df3=df.groupby('Genotype')['DAI3'].mean() 
    df5=df.groupby('Genotype')['DAI5'].mean()
    df7=df.groupby('Genotype')['DAI7'].mean()
    df9=df.groupby('Genotype')['DAI9'].mean()
    dfp=df3.to_frame().join(df5.to_frame()).join(df7.to_frame()).join(df9.to_frame())
    dfp.reset_index(inplace = True)
    dfh=dfp
    dfh = dfh.set_index(['Genotype'])

    sns.set()
    fig, ax = plt.subplots(figsize=(10,10)) 
    ax=sns.heatmap(dfh, cmap="coolwarm", annot=True, annot_kws={"size": 11})
    #ax.set_title('Disease Evaluation at different days after inoculation among tested genotypes', fontsize = 15)
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    ax.set_xticklabels(ax.get_xmajorticklabels(), fontsize = 13)
    ax.set_yticklabels(ax.get_ymajorticklabels(), fontsize = 13)
    plt.xlabel('Disease Evaluation- DAI (days after inoculation)', fontsize = 13)
    plt.ylabel('Genotype', fontsize = 13)
    img_html2 = getCurrFigAsBase64HTML2();
    
    # researcher tool, expected disease among genotypes
    conn = sql.connect("GHdata.db")
    cursor = conn.execute("select * from Greenhousedata")
    c= conn.cursor()

    df1 = pd.DataFrame(cursor.fetchall(),columns = ['GenotypeNumber','Genotype','rep','exp','DAI3','DAI5','DAI7','DAI9'], dtype=float) 
    convert_dict = {'GenotypeNumber': str, 
                    'Genotype':  str,
                   } 

    df = df1.astype(convert_dict) 
    df['DAI53']=df['DAI5']-df['DAI3']
    df['DAI75']=df['DAI7']-df['DAI5']
    df['DAI97']=df['DAI9']-df['DAI7']

    df53=df.groupby('Genotype')['DAI53'].mean()
    df53=pd.DataFrame(df53)
    df53.reset_index(inplace = True)

    plt.figure(figsize=(5,5), dpi= 80)
    plt.hlines(y=df53.index, xmin=0, xmax=df53.DAI53)
    for x, y, tex in zip(df53.DAI53, df53.index, df53.DAI53):
        t = plt.text(x, y, round(tex, 3),
                     verticalalignment='center', fontdict={'color':'red', 'size':10})

    plt.yticks(df53.index, df53.Genotype, fontsize=12)
    plt.title('[B-1]DAI3 to DAI5', fontdict={'size':12})
    plt.ylabel('  ', fontsize = 10)
    plt.grid(linestyle='--', alpha=1)
    plt.xlim(0, 0.2)
    plt.show()
    img_html3 = getCurrFigAsBase64HTML3();




    df75=df.groupby('Genotype')['DAI75'].mean()
    df75=pd.DataFrame(df75)
    df75.reset_index(inplace = True)

    plt.figure(figsize=(5,5), dpi= 80)
    plt.hlines(y=df75.index, xmin=0, xmax=df75.DAI75)
    for x, y, tex in zip(df75.DAI75, df75.index, df75.DAI75):
        t = plt.text(x, y, round(tex, 3),
                     verticalalignment='center', fontdict={'color':'purple', 'size':10})

    plt.yticks(df75.index, df75.Genotype, fontsize=12)
    plt.title('[B-2] DAI5 to DAI7', fontdict={'size':12})
    plt.ylabel(' ', fontsize = 10)
    plt.grid(linestyle='--', alpha=1)
    plt.xlim(0, 0.2)
    plt.show()
    img_html4 = getCurrFigAsBase64HTML4();

    df97=df.groupby('Genotype')['DAI97'].mean()
    df97=pd.DataFrame(df97)
    df97.reset_index(inplace = True)

    plt.figure(figsize=(5,5), dpi= 80)
    plt.hlines(y=df97.index, xmin=0, xmax=df97.DAI97)
    for x, y, tex in zip(df97.DAI97, df97.index, df97.DAI97):
        t = plt.text(x, y, round(tex, 3),
                     verticalalignment='center', fontdict={'color':'blue', 'size':10})

    plt.yticks(df97.index, df97.Genotype, fontsize=12)
    plt.title('[B-3]DAI7 to DAI9', fontdict={'size':12})
    plt.ylabel(' ', fontsize = 10)
    plt.grid(linestyle='--', alpha=1)
    plt.xlim(0, 0.2)
    plt.show()    
    img_html5 = getCurrFigAsBase64HTML5();

    # correlation data
    # read field data
    field = pd.read_csv('field_INFO8000.txt', delim_whitespace=True)
    field = field.drop('REP', 1)
    field = field.rename(columns={"TRT": "Genotype"})
    m1 = field.groupby('Genotype')['WM1'].mean().to_frame()
    m2 = field.groupby('Genotype')['WM2'].mean().to_frame()
    m3 = field.groupby('Genotype')['WM3'].mean().to_frame()
    m4 = field.groupby('Genotype')['WM4'].mean().to_frame()
    m5 = field.groupby('Genotype')['WM5'].mean().to_frame()
    m6 = field.groupby('Genotype')['WM6'].mean().to_frame()

    field_2018 = m1.merge(m2, left_index=True, right_index=True).merge(m3, left_index=True, right_index=True)
    field_2018 = field_2018.merge(m4, left_index=True, right_index=True).merge(m5, left_index=True, right_index=True)
    field_2018= field_2018.merge(m6, left_index=True, right_index=True)

    field_2018['mean'] = field_2018.mean(axis=1)
    field_2018 = field_2018.drop(columns=['WM1', 'WM2', 'WM3', 'WM4', 'WM5', 'WM6'])
    field_2018.reset_index(inplace = True)
    field_2018 = field_2018.set_index('Genotype')
    field_2018 = field_2018.drop(['594','680','703', '765'])
    field_2018['Genotype']=field_2018.index
    field_2018.index.names = ['index']

    # read researcher raw data
    conn = sql.connect("GHdata.db")
    cursor = conn.execute("select * from Greenhousedata")
    c= conn.cursor()

    df1 = pd.DataFrame(cursor.fetchall(),columns = ['GenotypeNumber','Genotype','rep','exp','DAI3','DAI5','DAI7','DAI9'], dtype=float) 
    convert_dict = {'GenotypeNumber': str, 
                    'Genotype':  str,
                   } 
    df = df1.astype(convert_dict) 

    df3=df.groupby('Genotype')['DAI3'].mean()
    df5=df.groupby('Genotype')['DAI5'].mean()
    df7=df.groupby('Genotype')['DAI7'].mean()
    df9=df.groupby('Genotype')['DAI9'].mean()
    dfp=df3.to_frame().join(df5.to_frame()).join(df7.to_frame()).join(df9.to_frame())
    dfp.reset_index(inplace = True)
    dfh_n = dfp
    dfh_n["Genotype"] = dfh_n["Genotype"].apply(str)



    dfr = dfh_n.merge(field_2018, left_on='Genotype', right_on='Genotype', suffixes=('_left', '_right'))
    dfr=dfr.drop('Genotype', axis=1)
    dfr =dfr.rename(columns={'mean': 'field'})

    dfr = dfr.round(2)
    plt.figure(figsize=(.3,.3))
    sns.pairplot(dfr)
    
    img_html7 = getCurrFigAsBase64HTML7();

    #'Correlation between Field and Greehouse')
    plt.matshow(dfr.corr(), cmap='Reds')
    plt.xticks(range(len(dfr.columns)), dfr.columns)
    plt.yticks(range(len(dfr.columns)), dfr.columns)
    plt.colorbar()
    plt.show() 
    
    img_html8 = getCurrFigAsBase64HTML8();    
        
    return '<br>' + img_html2+ '<br>''<br>' + img_html3+ '<br><br>' + img_html4+ '<br><br>' + img_html5+'<br><br>' + img_html7+'<br><br><br>' + img_html8


@app. route('/init')
def init():
    try: 
        conn = sql.connect("GHdata.db")
        conn.execute ("""
        drop table if exists Greenhousedata
        """)
        conn.execute ("""
        CREATE TABLE Greenhousedata (GenotypeNumber,Genotype,rep,exp,DAI3,DAI5,DAI7,DAI9);
        """)
        cursor = conn.execute("select * from Greenhousedata")
        c= conn.cursor()
        df2 = pd.read_excel("INFO8000Final_RawData_2Exp.xlsx")
        df3 = df2.round(decimals = 3)
        df3.to_sql("Greenhousedata", conn, if_exists='append', index=False)
        msginit = "Succeeded"
    except:
        msginit = "Failed"
    return render_template ('Init.html',msg=msginit)





@app.route('/forecast',  methods=['POST', 'GET'])
def forecast():
    
     if request.method == 'POST':
        try:
            Field_Genotype = request.form['Field_Genotype']
            Lesion = request.form['Lesion'] or "0"
            City = request.form["City"] or "Athens"
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
            d1temp= f'{(d1tempk - 273.15):.2f}'
            d2temp= f'{(d2tempk - 273.15):.2f}'
            d3temp= f'{(d3tempk - 273.15):.2f}'
            d4temp= f'{(d4tempk - 273.15):.2f}'
            d5temp= f'{(d5tempk - 273.15):.2f}'
           # msg1 = "day 1 time: " + str(d1dt_txt) + ", weather: " + str(d1main)+ ", temp (min): "+ str(d1temp)
           # msg2 = "day 2 time: " + str(d2dt_txt) + ", weather: " + str(d2main)+ ", temp (min): "+ str(d2temp)
           # msg3 = "day 3 time: " + str(d3dt_txt) + ", weather: " + str(d3main)+ ", temp (min): "+ str(d3temp)
           # msg4 = "day 4 time: " + str(d4dt_txt) + ", weather: " + str(d4main)+ ", temp (min):"+ str(d4temp)
           # msg5 = "day 5 time: " + str(d5dt_txt) + ", weather: " + str(d5main)+ ", temp (min):"+ str(d5temp)
            
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
                
                con.execute ("""
                drop table if exists fielddata
                """)
                
                con.execute ("""
                CREATE TABLE fielddata (Field_Genotype,Lesion);
                """)
                
                cur.execute("INSERT INTO fielddata (Field_Genotype,Lesion) VALUES(?,?)",(Field_Genotype,Lesion))
                
                con.commit()
                
                msgrecord2 = "Record successfully added"
                
                cur.execute("select * from fielddata")
                data_field = pd.DataFrame(cur.fetchall(),columns = ['Field_Genotype','Lesion'])
                genotype = data_field.iloc[0,0]
                lesion = data_field.iloc[0,1]
                
                
                #Weather
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
                
                # The threshold 0.3 cm is based on the disease progress from previous study tested both in greenhouse and field trails which show significant difference between resistant and susceptible genotypes.
                
 # The threshold 0.3 cm is the disease progress from previous study tested both in greenhouse and field trails which show significant difference between resistant and susceptible genotypes.

                #if str(PD) > "51.94":
                if str(lesion) > "0.3":
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
                    elif str(d1temp) > "24":
                        if str(genotype) == "628":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "660":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "668":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "708":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        else:
                            msgsug= "Symptom of disease is observered, but it won't rain this week. Though temerperature might be higher than 24°C, the genotype of peanut is in low risk. Chemical is not neccessary now."
                    elif str(d2temp) > '24':
                        if str(genotype) == "628":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "660":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "668":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "708":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        else:
                            msgsug= "Symptom of disease is observered, but it won't rain this week. Though temerperature might be higher than 24°C, the genotype of peanut is in low risk. Chemical is not neccessary now."
                    elif str(d3temp) > '24':
                        if str(genotype) == "628":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "660":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "668":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "708":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        else:
                            msgsug= "Symptom of disease is observered, but it won't rain this week. Though temerperature might be higher than 24°C, the genotype of peanut is in low risk. Chemical is not neccessary now."
                    elif str(d4temp) > '24':
                        if str(genotype) == "628":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "660":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "668":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "708":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        else:
                            msgsug= "Symptom of disease is observered, but it won't rain this week. Though temerperature might be higher than 24°C, the genotype of peanut is in low risk. Chemical is not neccessary now."
                    elif str(d5temp) > '24':
                        if str(genotype) == "628":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "660":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "668":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        elif str(genotype) == "708":
                            msgsug= "Symptom of disease is observed. Though it won't rain this week, the genotype of peanut is in high risk. Chemical should be applied today. "
                        else:
                            msgsug= "Symptom of disease is observered, but it won't rain this week. Though temerperature is higher than 24°C, the genotype of peanut is in low risk. Chemical is not neccessary now."
                    else: 
                        msgsug= "Symptom of disease is observed, but it won't rain this week and the temperature might be lower than 24°C. Chemical is not necessary now. "
                else: 
                    msgsug= "Symptom of disease is not significant. Chemical is not necessary now."     
            
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
            
             # farmer tool, expected disease by genotype
            cur.execute("select * from fielddata")
            data_field = pd.DataFrame(cur.fetchall(),columns = ['Field_Genotype','Lesion'])
            genotype2 = data_field.iloc[0,0]
            lesion = data_field.iloc[0,1]
           
            conn = sql.connect("GHdata.db")
            cursor = conn.execute("select * from Greenhousedata")
            c= conn.cursor()

            df1 = pd.DataFrame(cursor.fetchall(),columns = ['GenotypeNumber','Genotype','rep','exp','DAI3','DAI5','DAI7','DAI9'], dtype=float) 
            convert_dict = {'GenotypeNumber': str, 
                            'Genotype':  str,
                           } 
            df = df1.astype(convert_dict) 
            df3=df.groupby('Genotype')['DAI3'].mean()
            df5=df.groupby('Genotype')['DAI5'].mean()
            df7=df.groupby('Genotype')['DAI7'].mean()
            df9=df.groupby('Genotype')['DAI9'].mean()
            dfp=df3.to_frame().join(df5.to_frame()).join(df7.to_frame()).join(df9.to_frame())
            dfp['Genotype']=['12Y','13M','628','630','660','668','683','694','695','696','704','708','730','736']
            #dfp.rename(index={0:'12Y',1:'13M',2:'628',3:'630',4:'660',5:'668',6:'683',7:'694',8:'695',9:'696',10:'704',11:'708',12:'730',13:'736'}, inplace=True)
            a= genotype2
            option=dfp['Genotype'] == a
            dfp_res=dfp[option]
            dfp_res = pd.DataFrame(dfp_res, columns = ['DAI3', 'DAI5', 'DAI7', 'DAI9'])
            dfp_res=dfp_res.T
            dfp_res['DAI']=[3,5,7,9]
            dfp_res.index.names = ['DAI']
            
            plt.close('all')
            sns.reset_orig()
            sns.set()
            sns.set(style="whitegrid")
            ax=sns.pointplot(data=dfp_res, x="DAI", y= a, color="#bb3f3f")
            ax.set_title("Predicted Disease Curve")
            
            plt.annotate('DAI: days after inoculation', (0,0), (0, -50), xycoords='axes fraction', textcoords='offset points', va='top')
            
            img_html6 = getCurrFigAsBase64HTML6();

            # farmers tool, expected disease at end of season by genotype           
            cur.execute("select * from fielddata")
            data_field = pd.DataFrame(cur.fetchall(),columns = ['Field_Genotype','Lesion'])
            genotype = data_field.iloc[0,0]
            lesion = data_field.iloc[0,1]
            
            field = pd.read_csv('field_INFO8000.txt', delim_whitespace=True)
            field = field.drop('REP', 1)
            field = field.rename(columns={"TRT": "Genotype"})
            m1 = field.groupby('Genotype')['WM1'].mean().to_frame()
            m2 = field.groupby('Genotype')['WM2'].mean().to_frame()
            m3 = field.groupby('Genotype')['WM3'].mean().to_frame()
            m4 = field.groupby('Genotype')['WM4'].mean().to_frame()
            m5 = field.groupby('Genotype')['WM5'].mean().to_frame()
            m6 = field.groupby('Genotype')['WM6'].mean().to_frame()

            field_2018 = m1.merge(m2, left_index=True, right_index=True).merge(m3, left_index=True, right_index=True)
            field_2018 = field_2018.merge(m4, left_index=True, right_index=True).merge(m5, left_index=True, right_index=True)
            field_2018= field_2018.merge(m6, left_index=True, right_index=True)

            field_2018['mean'] = field_2018.mean(axis=1)
            field_2018 = field_2018.drop(columns=['WM1', 'WM2', 'WM3', 'WM4', 'WM5', 'WM6'])
            field_2018.reset_index(inplace = True)
            field_2018 = field_2018.set_index('Genotype')
            field_2018 = field_2018.drop(['594','680','703', '765'])
            field_2018['Genotype']=field_2018.index
            field_2018.index.names = ['index']  
            
            conn = sql.connect("GHdata.db")
            cursor = conn.execute("select * from Greenhousedata")
            c= conn.cursor()

            df1 = pd.DataFrame(cursor.fetchall(),columns = ['GenotypeNumber','Genotype','rep','exp','DAI3','DAI5','DAI7','DAI9'], dtype=float) 
            convert_dict = {'GenotypeNumber': str, 
                            'Genotype':  str,
                           } 
            df = df1.astype(convert_dict) 

            df3=df.groupby('Genotype')['DAI3'].mean()
            df5=df.groupby('Genotype')['DAI5'].mean()
            df7=df.groupby('Genotype')['DAI7'].mean()
            df9=df.groupby('Genotype')['DAI9'].mean()
            dfp=df3.to_frame().join(df5.to_frame()).join(df7.to_frame()).join(df9.to_frame())
            dfp.reset_index(inplace = True)
            dfh_n = dfp
            dfh_n["Genotype"] = dfh_n["Genotype"].apply(str)



            dfr = dfh_n.merge(field_2018, left_on='Genotype', right_on='Genotype', suffixes=('_left', '_right'))
            dfr=dfr.drop('Genotype', axis=1)
            dfr =dfr.rename(columns={'mean': 'field'})

            dfr = dfr.round(2)               
                
                
            
             # farmers tool, expected disease at end of season by genotype
            corr_n = dfr.corr()
            corr_n = corr_n.drop(columns=['DAI3', 'DAI5', 'DAI7', 'DAI9'], index='field')

            corr_max = corr_n[corr_n.field == corr_n.field.max()]
            corr_max['select']=corr_max.index
            corr_max['select']=corr_max.select.str.extract('(\d+)')
            DAI_select=corr_max['select'].astype(int)
            DAI_select.reset_index(drop=True)

            x3=pd.DataFrame()
            x3['DE']=dfr['DAI3']
            x3['DAI']='3'
            x5=pd.DataFrame()
            x5['DE']=dfr['DAI5']
            x5['DAI']='5'
            x7=pd.DataFrame()
            x7['DE']=dfr['DAI7']
            x7['DAI']='7'
            x9=pd.DataFrame()
            x9['DE']=dfr['DAI9']
            x9['DAI']='9'

            dfr_reg = pd.concat([x3, x5, x7, x9], axis=0, join='outer')
            dfr_reg['DAI'] = dfr_reg['DAI'].astype(int)

            option= dfr_reg['DAI'] ==  DAI_select[0]
            dfr_reg=dfr_reg[option]
            dfr_reg['y']=dfr['field']
            dfr_reg.drop(columns='DAI', inplace= True)
            dfr_reg.rename(columns={'DE':'x'},inplace=True)

            fit1 = sm.GLM(dfr_reg['y'].astype(float), dfr_reg['x'].astype(float))
            fit1_res = fit1.fit()
            
            lesion1=float(lesion)
            
            a=lesion1 
            PD = fit1_res.params[0]*a
            PD = PD.round(2)
            msg_predict = str(PD)
            
            
            
            return render_template("WeatherResult.html",msgrecord2=msgrecord2,msg_predict=msg_predict, rows2 =rows2,rows5=rows5,msgsug=msgsug) + '<br>' +' <h3> E. Predicted disease curve in early days. Genotype :  '+ genotype2 + '</h3>'  + img_html6  + '<br>' 
            con.close()
            


    




