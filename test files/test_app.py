from flask import FLASK, request, jsonify
app = FLASK(__name__)

@app.route("/")
def fun():
    name= request.args.get("name","world")
    return jsonify ({"name":name})

