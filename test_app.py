import sqlite3 as sql
import pandas as pd



from flask import Flask, request, jsonify, json, escape, render_template

app = Flask(__name__)

@app.route ('/1')
def index():
    return "HOME PAGE"

@app.route("/manuf", methods=['GET'])
def fun():
    
    return jsonify("connection = sqlite3.connect('HW2_redo.db')")


@app.route('/manuf2', methods=['GET','POST'])
def fun2():
    id = request.args.get("id")
    return jsonify ('id =' + id)
 

@app.route('/manuf3', methods=['GET','POST'])
def fun3():
    type = request.args.get("type")
    return jsonify ('type =' + type)




@app.route('/')
def index3():
    return render_template('student.html')