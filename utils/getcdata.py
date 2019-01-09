# getcdata.py - fetch the calibrated data from the AS7265x module
# this program is 3-clause BSD license
import serial as ser
from parse import *
import pandas as pd
import numpy as np

#global variables
uartpath = '/dev/ttyUSB0'
uartbaud = 115200
uarttout = 5

print('getcdata')
print('This utility is part of the TeraHz project')

wavelens = pd.Series([410, 435, 460, 485, 510, 535, 560, 585, 610, 645, 680, 705, 730, 760, 810, 860, 900, 940],
                    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'R', 'I', 'S', 'J', 'T', 'U', 'V', 'W', 'K', 'L'])

wavetable = pd.DataFrame(columns=wavelens)

with ser.Serial(uartpath, uartbaud, timeout=uarttout) as sensor:
    sensor.write(b'ATCDATA\n')
    response = sensor.readline()
    print(response.decode())
    parsed = parse('{:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f}, {:f} OK', response.decode())
    print(parsed)
