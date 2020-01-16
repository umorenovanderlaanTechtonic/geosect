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
    polygons = []

    for item in coords:
        #check we have a polygon
        geometry = item['geometry']
        if geometry['type'] != 'Polygon':
            return 'Please use a valid polygon'

        #create list of polygon coordinates
        coordinates = geometry['coordinates']
        polygons.append(Polygon(coordinates[0]))
    
    #check if polygons intersect
    intersect = polygons[0].intersects(polygons[1])
    
    if intersect == True:
        return 'These polygons intersect!'
    else:
        return 'These polygons do not intersect.'

if __name__ == '__main__':
    app.run()