from flask import Flask, render_template, request, redirect, jsonify
from shapely.geometry import Polygon
import json
import geojson

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/geosect', methods = ['POST'])
def geosect():
    # get form data
    data = request.get_json()
    coords =  list(data.values())


    return data

if __name__ == '__main__':
    app.run()