from flask import Flask
from flask import jsonify
import json
import os
import csv
from flask_cors import CORS

app= Flask(__name__)
CORS(app)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    with open(os.path.join("static","samples.json")) as file:
        data = json.load(file)
    return data
    
if __name__=="__main__":
    app.run(debug=True)