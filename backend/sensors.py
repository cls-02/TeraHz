# sensors.py - a module for interfacing to the sensors
# Copyright 2019 Kristjan Komloši
# The code in this file is licensed under the 3-clause BSD License

import serial as ser
import pandas as pd
from threading import Timer
from sys import exit as ex

class Spectrometer:
    def schedule(self, delay):
        self.timerObject=Timer(delay, retrieveData)

    def __init__(self, path='/dev/ttyAMA0', baudrate=115200, timeout=1, refreshrate=1):
        self.path=path
        self.baudrate=baudrate
        self.timeout=1
        try:
            self.serialObject = ser.Serial(path, baudrate, timeout)
        except:
            print('An exception occured when opening the serial port at {}'.format(path))
            ex(1)
        else:
            initialiseSensor()
            startDataCollection()
