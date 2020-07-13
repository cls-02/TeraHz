# app.py - main backend program
'''Main TeraHz backend program'''
# All code in this file is licensed under the ISC license, provided in LICENSE.txt
from flask import Flask, jsonify
import .terahz

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


@app.route('/')
def renderTable():
    wavelengthDict = {
        'A': '410 nm',
        'B': '435 nm',
        'C': '460 nm',
        'D': '485 nm',
        'E': '510 nm',
        'F': '535 nm',
        'G': '560 nm',
        'H': '585 nm',
        'R': '610 nm',
        'I': '645 nm',
        'S': '680 nm',
        'J': '705 nm',
        'T': '730 nm',
        'U': '760 nm',
        'V': '810 nm',
        'W': '860 nm',
        'K': '900 nm',
        'L': '940 nm'}
    data = [s.getData(), l.getData(), u.getABI()]
    return render_template('index.html', data = data, wavelengths = wavelengthDict)
