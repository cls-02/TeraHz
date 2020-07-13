# app.py - main backend program
'''Main TeraHz backend program'''
# All code in this file is licensed under the ISC license, provided in LICENSE.txt
from flask import Flask, jsonify
import sensors

app = Flask(__name__)
@app.route('/data')
def sendData():
    '''Responder function for /data route'''
    s = sensors.Spectrometer(path='/dev/serial0')
    u = sensors.UVSensor()
    l = sensors.LxMeter()
    response = jsonify([s.getData(), l.getData(), u.getABI()])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
