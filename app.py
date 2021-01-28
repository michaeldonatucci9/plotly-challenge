from flask import Flask
from flask import jsonify
from flask import render_template
import json
import os
import csv
import plotly_express as px

app= Flask(__name__)


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