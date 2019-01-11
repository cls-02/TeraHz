# getcdata.py - fetch the calibrated data from the AS7265x module
# this program is 3-clause BSD license
import serial as ser
from parse import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
#global variables
uartpath = '/dev/ttyUSB0'
uartbaud = 115200
uarttout = 5

wl = [410, 435, 460, 485, 510, 535, 560, 585, 610, 645, 680, 705, 730, 760, 810, 860, 900, 940]
responseorder = [i for i in 'RSTUVWGHIJKLABCDEF'] # works, do NOT touch!
realorder = [i for i in 'ABCDEFGHRISJTUVWKL']
plt.ion()

print('getcdata')
print('This utility is part of the TeraHz project')

wavelens = pd.Series(realorder)
data=pd.DataFrame([], [])

wavetable = pd.DataFrame(columns=realorder)
graph=plt.figure()
plot=graph.add_subplot(111)
with ser.Serial(uartpath, uartbaud, timeout=uarttout) as sensor:
    while True:
        sensor.write(b'ATCDATA\n')
        rawresp = sensor.readline().decode()
        # parses, calculates and saves the data
        response = pd.Series([float(i)/35.0 for i in rawresp[:-3].split(',')], index=responseorder)
        data = pd.DataFrame(response, index=realorder, columns = ['uW/cm^2']) # puts data into a DataFrame
        data.insert(0, 'wavelenght', wl) #inserts a legend
        print(data)
        plot.cla()
        line=plot.plot(data['wavelenght'], data['uW/cm^2'])
        graph.canvas.draw()
        time.sleep(1)
