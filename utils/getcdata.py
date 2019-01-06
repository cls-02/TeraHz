import serial as ser
with ser.Serial('/dev/ttyUSB0', 115200, timeout=5) as serport:
    serport.write(b'ATCDATA\n')
    print(serport.readline())
