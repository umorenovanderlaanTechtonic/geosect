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
    data = request.get_json()
    response = ''
    try:
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
            response = 'These polygons intersect!'
        else:
            response = 'These polygons do not intersect.'
    except:
        response = 'Please use a valid geojson object'
    return response

if __name__ == '__main__':
    app.run()