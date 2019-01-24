# sensors.py - a module for interfacing to the sensors
# Copyright 2019 Kristjan Komloši
# The code in this file is licensed under the 3-clause BSD License

import serial as ser
import pandas as pd
from threading import Timer
from sys import exit as ex
import time

class Spectrometer:
    def initializeSensor(self):
        '''confirm the sensor is responding and proceed with spectrometer initialization'''
        try:
            rstring='undefined' # just need it set to a value
            self.serialObject.write(b'AT\n')
            rstring=self.serialObject.readline().decode()
            if rstring == 'undefined':
                raise Exception #sensor didn't respond
            if rstring == 'OK':
                pass #handshake passed
            if rstring == 'ERROR':
                raise Exception #sensor is in error state
        except:
            print('An exception ocurred when performing spectrometer handshake')
            ex(1)
        self.setParameters()

    def setParameters(self):
        '''applies the parameters like LED light and gain to the spectrometer'''
        try:
            if 'it_time' in self.parameters:
                it_time = int(self.parameters['it_time'])
                if it_time <=0 :
                    it_time = 1
                self.serialObject.write('ATINTTIME={}\n'.format(string(it_time)).encode())
                self.serialObject.readline()

            if 'gain' in self.parameters:
                gain = int(self.parameters['gain'])
                if gain < 0 or gain > 3:
                    gain = 1
                self.serialObject.write('ATGAIN={}\n'.format(gain).encode())
                self.serialObject.readline()

            if 'led' in self.parameters:
                led = bool(self.parameters['led'])
                if led:
                    led=1
                else:
                    led=0
                self.serialObject.write('ATLED3={}\n'.format(led).encode())
                self.serialObject.readline()
        except:
           print('An exception occured during spectrometer initialization')
           ex(1)

    def startDataCollection(self):
        try:
            self.serialObject.write(b'ATCDATA\n')
            rawresp = self.serialObject.readline().decode()
        except:
            print('An exception occurred when polling for spectrometer data')
            ex(1)
        else:
            responseorder = [i for i in 'RSTUVWGHIJKLABCDEF']
            realorder = [i for i in 'ABCDEFGHRISJTUVWKL']
            response = pd.Series([float(i)/35.0 for i in rawresp[:-3].split(',')], index=responseorder)
            self.data = pd.DataFrame(response, index=realorder, columns = ['uW/cm^2'])
        self.schedule(self.rrate)

    def schedule(self, refresh):
        self.timerObject = Timer(refresh, self.startDataCollection)
        self.timerObject.start()


    def __init__(self, path='/dev/ttyUSB0', baudrate=115200, tout=1, rrate=1, params={}):
        self.path = path
        self.baudrate = baudrate
        self.timeout = 1
        self.rrate = rrate
        self.parameters = params
        try:
            self.serialObject = ser.Serial(path, baudrate, timeout=tout)
        except:
            print('An exception occured when opening the serial port at {}'.format(path))
            ex(1)
        else:
            self.initializeSensor()
            self.startDataCollection()
