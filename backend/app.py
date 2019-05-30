# All code in this file is licensed under the ISC license, provided in LICENSE.txt
from flask import Flask, redirect, url_for, request
import flask
import sensors
import json
app = Flask(__name__)
s=sensors.Spectrometer(path='/dev/serial0', baudrate=115200, tout=1)
u=sensors.UVSensor()
l=sensors.LxMeter()

@app.route('/data')
def sendData():
    response = flask.jsonify([s.getData(), l.getData(), u.getABI()])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
