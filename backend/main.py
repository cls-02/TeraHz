from flask import Flask, redirect, url_for, request
import sensors
import json
app = Flask(__name__)
s=sensors.Spectrometer(path='/dev/ttyAMA0', baudrate=115200, tout=1)
u=sensors.UVSensor()
l=sensors.LxMeter()

@app.route('/data')
def sendData():
    return json.dumps([s.getData(), l.getData(), u.getABI])
