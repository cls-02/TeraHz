# sensors.py - a module for interfacing to the sensors
# Copyright 2019 Kristjan Komloši
# The code in this file is licensed under the 3-clause BSD License

import serial as ser
import pandas as pd
import smbus2
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
            raise Exception('An exception ocurred when performing spectrometer handshake')
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
           raise Exception('An exception occured during spectrometer initialization')
           ex(1)

    def refreshData(self):
        try:
            self.serialObject.write(b'ATCDATA\n')
            rawresp = self.serialObject.readline().decode()
        except:
            raise Exception('An exception occurred when polling for spectrometer data')
            ex(1)
        else:
            responseorder = [i for i in 'RSTUVWGHIJKLABCDEF']
            realorder = [i for i in 'ABCDEFGHRISJTUVWKL']
            response = pd.Series([float(i)/35.0 for i in rawresp[:-3].split(',')], index=responseorder)
            self.data = pd.DataFrame(response, index=realorder, columns = ['uW/cm^2'])


    def __init__(self, path='/dev/ttyUSB0', baudrate=115200, tout=1, rrate=1, params={}):
        self.path = path
        self.baudrate = baudrate
        self.timeout = 1
        self.parameters = params
        try:
            self.serialObject = ser.Serial(path, baudrate, timeout=tout)
        except:
            raise Exception('An exception occured when opening the serial port at {}'.format(path))
            ex(1)
        else:
            self.initializeSensor()
            self.startDataCollection()


class LxMeter:
    def __init__(self, busNumber=1, addr=0x39):
        self.addr = address
        try:
            self.bus = smbus2.SMBus(busNumber) # initialize the SMBus interface
        except:
            raise Exception('An exception occured opening the SMBus {}'.format(self.bus))

        try:
            self.bus.write_byte_data(addr, 0xa0, 0x03) # enable the sensor
        except:
            raise Exception('An exception occured when enabling lux meter')

    def setGain(self, gain):
        '''Set the sensor gain. Either 1 or 16.'''
        if gain == 1:
            try:
                temp = self.bus.read_byte_data(addr, 0xa1)
                self.bus.write_byte_data(addr, 0xa1, 0xef & temp)
            except:
                raise Exception('An exception occured when setting lux meter gain')
        if gain == 16:
            try:
                temp = self.bus.read_byte_data(addr, 0xa1)
                self.bus.write_byte_data(addr, 0xa1, 0x10 | temp)
            except:
                raise Exception('An exception occured when setting lux meter gain')
        else:
            raise Exception('Invalid gain')

    def getGain(self):
        '''Get the gain from the sensor.'''
        try:
            if self.bus.read_byte_data(addr, 0xa1) & 0x10 == 0x10:
                return 16
            if self.bus.read_byte_data(addr, 0xa1) & 0x10 == 0x00:
                return 1
        except:
            raise Exception('An error occured when getting lux meter gain')

    def setIntTime(self, time):
        '''Set the lux sensor integration time. 0 to including 2'''
        if time < 0 or time > 2:
            raise Exception('Invalid integration time')
        try:
            temp = self.bus.read_byte_data(addr, 0xa1)
            self.bus.write_byte_data(addr, 0xa1, (temp & 0xfc) | time)
        except:
            raise Exception('An error occured setting lux integration time')

    def getIntTime(self):
        '''Get the lux sensor integration time.'''
        try:
            return self.bus.read_byte_data(addr, 0xa1) & 0xfc
        except:
            raise Exception('An error occured getting lux integration time')

    def getData(self):
        '''return the calculated lux value'''
        try:
            chA = self.bus.read_word_data(addr, 0xac)
            chB = self.bus.read_word_data(addr, 0xae)
        except:
            raise Exception('An error occured fetching lux channels')

        if chB/chA <= 0.5 and chB/chA > 0:
            lux = (0.0304*chA) - (0.062*chA*((chB/chA)**1.4))
        elif chB/chA <= 0.61 and chB/chA > 0.5:
            lux = (0.0224*chA) - (0.031*chB)
        elif chB/chA <=0.8 and chB/chA > 0.61:
            lux = (0.0128*chA) - (0.0153*chB)
        elif chB/chA <=1.3 and chB/chA >0.8:
            lux = (0.00146*chA) - (0.00112*chB)
        else:
            lux = 0
        return lux
