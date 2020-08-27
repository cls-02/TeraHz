# app.py - main backend program
'''Main TeraHz backend program'''
# All code in this file is licensed under the ISC license, provided in LICENSE.txt
from flask import Flask, jsonify, render_template
from . import terahz

def start_flaskapp():
    '''Initialize global variables'''
    global app, s, u, l
    app = Flask(__name__)
    s = terahz.Spectrometer(path='/dev/serial0')
    u = terahz.UVSensor()
    l = terahz.LxMeter()

@app.route('/data')
def sendData():
    '''Responder function for /data route'''
    response = jsonify([s.getData(), l.getData(), u.getABI()])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/')
def renderTable():
    ''''Main page renderer'''
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
    return render_template('index.html', data=data, wavelengths=wavelengthDict)
