# sensors.py - a module for interfacing to the sensors
'''Module for interfacing with TeraHz sensors'''
# Copyright 2019 Kristjan Komloši
# All code in this file is licensed under the ISC license, provided in LICENSE.txt
import serial as ser
import pandas as pd
import smbus2





class Spectrometer:
    '''Class representing the AS7265X specrometer'''

    def initializeSensor(self):
        '''confirm the sensor is responding and proceed\
         with spectrometer initialization'''
        try:
            rstring = 'undefined'  # just need it set to a value
            self.setParameters({'gain': 0})
            self.serialObject.write(b'AT\n')
            rstring = self.serialObject.readline().decode()
            if rstring == 'undefined':
                raise Exception  # sensor didn't respond
            if rstring == 'OK':
                pass  # handshake passed
            if rstring == 'ERROR':
                raise Exception  # sensor is in error state
        except:
            raise Exception('No AT command response')

    def setParameters(self, parameters):
        '''applies the parameters like LED light and gain to the spectrometer'''
        try:
            if 'it_time' in parameters:
                it_time = int(parameters['it_time'])
                if it_time <= 0:
                    it_time = 1
                self.serialObject.write(
                    'ATINTTIME={}\n'.format(str(it_time)).encode())
                self.serialObject.readline()

            if 'gain' in parameters:
                gain = int(parameters['gain'])
                if gain < 0 or gain > 3:
                    gain = 1
                self.serialObject.write('ATGAIN={}\n'.format(gain).encode())
                self.serialObject.readline()

            if 'led' in parameters:
                led = bool(parameters['led'])
                if led:
                    led = 1
                else:
                    led = 0
                self.serialObject.write('ATLED3={}\n'.format(led).encode())
                self.serialObject.readline()
        except:
            raise Exception('Error setting spectrometer parameters')

    def getData(self):
        '''Returns spectral data in a pandas DataFrame.'''
        try:
            self.serialObject.write(b'ATCDATA\n')
            rawresp = self.serialObject.readline().decode()
        except:
            raise Exception('Error polling spectrometer data')
        else:
            responseorder = list('RSTUVWGHIJKLABCDEF')
            realorder = list('ABCDEFGHRISJTUVWKL')
            response = pd.Series(
                [float(i) / 35.0 for i in rawresp[:-3].split(',')], index=responseorder)
            return pd.DataFrame(response, index=realorder, columns=['uW/cm^2']).to_dict()['uW/cm^2']

    def __init__(self, path='/dev/ttyUSB0', baudrate=115200, tout=1):
        self.path = path
        self.baudrate = baudrate
        self.timeout = 1
        try:
            self.serialObject = ser.Serial(path, baudrate, timeout=tout)
        except:
            raise Exception('Error opening serial port: {}'.format(path))
        else:
            self.initializeSensor()


class LxMeter:
    '''Class representing the APDS-9301 digital photometer.'''

    def __init__(self, busNumber=1, addr=0x39):
        self.addr = addr
        try:
            # initialize the SMBus interface
            self.bus = smbus2.SMBus(busNumber)
        except:
            raise Exception(
                'Error opening SMBus {}'.format(self.bus))

        try:
            self.bus.write_byte_data(
                self.addr, 0xa0, 0x03)  # enable the sensor
            self.setGain(16)
        except:
            raise Exception('Error enabling lux meter')

    def setGain(self, gain):
        '''Set the sensor gain. Either 1 or 16.'''
        if gain == 1:
            try:
                temp = self.bus.read_byte_data(self.addr, 0xa1)
                self.bus.write_byte_data(self.addr, 0xa1, 0xef & temp)
            except:
                raise Exception('Error setting lux meter gain')
        if gain == 16:
            try:
                temp = self.bus.read_byte_data(self.addr, 0xa1)
                self.bus.write_byte_data(self.addr, 0xa1, 0x10 | temp)
            except:
                raise Exception('Error setting lux meter gain')
        else:
            raise Exception('Invalid gain')

    def getGain(self):
        '''Get the gain from the sensor.'''
        try:
            if self.bus.read_byte_data(self.addr, 0xa1) & 0x10 == 0x10:
                return 16
            if self.bus.read_byte_data(self.addr, 0xa1) & 0x10 == 0x00:
                return 1
            raise Exception('An error occured when getting lux meter gain')
            # Under normal conditions, this raise is unreachable.
        except:
            raise Exception('An error occured when getting lux meter gain')

    def setIntTime(self, time):
        '''Set the lux sensor integration time. 0 to including 2'''
        if time < 0 or time > 2:
            raise Exception('Invalid integration time')
        try:
            temp = self.bus.read_byte_data(self.addr, 0xa1)
            self.bus.write_byte_data(self.addr, 0xa1, (temp & 0xfc) | time)
        except:
            raise Exception(
                'An exception occured setting lux integration time')

    def getIntTime(self):
        '''Get the lux sensor integration time.'''
        try:
            return self.bus.read_byte_data(self.addr, 0xa1) & 0x03
        except:
            raise Exception(
                'An exception occured getting lux integration time')

    def getData(self):
        '''return the calculated lux value'''
        try:
            chA = self.bus.read_word_data(self.addr, 0xac)
            chB = self.bus.read_word_data(self.addr, 0xae)
        except:
            raise Exception('An exception occured fetching lux channels')

        # Refer to APDS-9301 datasheet!
        if chB / chA <= 0.5 and chB / chA > 0:
            lux = 0.0304 * chA - 0.062 * chA * (chB / chA)**1.4
        elif chB / chA <= 0.61 and chB / chA > 0.5:
            lux = 0.0224 * chA - 0.031 * chB
        elif chB / chA <= 0.8 and chB / chA > 0.61:
            lux = 0.0128 * chA - 0.0153 * chB
        elif chB / chA <= 1.3 and chB / chA > 0.8:
            lux = 0.00146 * chA - 0.00112 * chB
        else:
            lux = 0
        return lux


class UVSensor:
    '''Class representing VEML6075 UVA/B meter'''

    def __init__(self, bus=1, addr=0x10):
        self.addr = addr
        try:
            self.bus = smbus2.SMBus(bus)
        except:
            raise Exception(
                'An exception occured opening SMBus {}'.format(bus))

        try:
            # enable the sensor and set the integration time
            self.bus.write_byte_data(self.addr, 0x00, 0b00010000)

            # trigger a measurement to prevent bus errors at first read
            self.bus.write_byte_data(self.addr, 0x00, 0b00010010)  # UV_AF=1
            self.bus.write_byte_data(self.addr, 0x00, 0b00010110)  # UV_TRIG=1
            self.bus.write_byte_data(
                self.addr, 0x00, 0b00010000)  # normal mode

        except:
            raise Exception(
                'Error initalizing the UV Sensor')

    def getABI(self):
        '''Calculates the UVA and UVB irradiances,
        along with UV index. Returns [a,b,i]'''

        try:
            # read the raw UVA, UVB and compensation values from the sensor
            aRaw = self.bus.read_word_data(self.addr, 0x07)
            bRaw = self.bus.read_word_data(self.addr, 0x09)
            c1 = self.bus.read_word_data(self.addr, 0x0a)
            c2 = self.bus.read_word_data(self.addr, 0x0b)
        except:
            raise Exception('Error fetching raw UV data')
        # Refer to Vishay app note 84339 and Sparkfun VEML6075 documentation.
        # The computed values may be negative if UV is vastly weaker than
        # visible and IR light. This is not a bug!

        a = (aRaw - 2.22 * c1 - 1.33 * c2) * 1.06
        b = (bRaw - 2.95 * c1 - 1.74 * c2) * 0.48
        i = (a + b) / 2  # calculate UV index
        return [a, b, i]

    def on(self):
        '''Turns the UV sensor on after shutdown.'''
        try:
            # write the default value for power on
            # no configurable params = no bitmask
            self.bus.write_byte_data(self.addr, 0x00, 0x10)
        except:
            raise Exception(
                'Error turning the UV sensor on')

    def off(self):
        '''Shuts the UV sensor down.'''
        try:
            # write the default value + the shutdown bit
            # no configurable params = no bitmask
            self.bus.write_byte_data(self.addr, 0x00, 0x11)
        except:
            raise Exception(
                'Error shutting the UV sensor down')
