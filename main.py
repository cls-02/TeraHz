#main.py - the main program file of the TeraHz project
#This code is licensed under 3-clause BSD licensed
import serial as ser

#global config
# TODO: move this to another file
uartpath = '/dev/ttyUSB0'
uartbaud = 115200
uarttout = 5

print('TeraHz project')
print('Accessing the serial port')

sp =  'blank'

try:
    sp = ser.Serial(uartpath, uartbaud, timeout=uarttout)
except Exception as e:
    print('Connection to serial port at {} failed!'.format(uartpath))
    raise e
    exit()
