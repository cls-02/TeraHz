# TeraHz Electrical Guide
This section briefly explains the neccessary electrical connections between the
Raspberry Pi and the sensors you'll need to make to ensure correct and safe
operation.

As mentioned before, TeraHz requires 3 sensors to operate. The simpler UVA/UVB
sensor and the ambient light analyzer connect to the Raspberry's SMBus (I2C)
bus, while the spectrometer connects via high-speed UART.

![pinout](imgs/raspi-pinout.png)

## PCBs vs breakout boards & jumpers
The Raspberry Pi GPIO port includes enough power pins to require only jumper
cables to connect the sensors to the Raspberry Pi. However, this is not a great
idea. During development, jumper cables have repeatedly been proven to be an
unreliable nuisance, and their absolute lack of rigidity helped me fry one of my
development Raspberry Pis. For this reason, I wholeheartedly recommend using a
simple PCB to route the connections from the Pi to the sensors. At this time,
there is no official TeraHz PCB, but it shall be announced and included in the
project when basic testing will be done.

GPIO can be routed to the PCB with a standard old IDE disk cable, and terminated
with another 40-pin connector at the PCB. Sensor breakouts should be mounted
<<<<<<< HEAD
through standard 0.1" connectors, male on the sensor breakout and female on the
PCB. A shitty add-on header and a shitty add-on header v1.69bis can't hurt, either.
=======
through standard 0.1" connectors, male on the sensor brakout and female on the
PCB. A shitty addon header and a shitty addon header v1.69bis can't hurt, either.
>>>>>>> fd1f07d40dace3e003e49377d4771de53f8bdeb8

## SMBus sensors
SMBus is a well-defined version of the well-known I2C bus, widely used
in computer motherboards for low-band bandwidth communication with various ICs,
especially sensors and power-supply related devices. This bus is broken out on
the Raspberry Pi GPIO port as the "I2C1" bus (see picture).

Pins are familiarly marked as SDA and SCL, the same as with classic I2C. They
connect to the SDA and SCL pins on the VEML6075 and APDS-9301 sensor.

## UART sensor
<<<<<<< HEAD
Spectral sensor attaches through the UART port on the Raspberry pi (see picture).
=======
Spectrometry sensor attaches through the UART port on the Raspberry pi (see picture).
>>>>>>> fd1f07d40dace3e003e49377d4771de53f8bdeb8

The Tx and Rx lines must cross over, connecting the sensor's Tx line to the
computer's Rx line and vice versa.

## Power supply
As the sensors require only a small amount of power, they can be powered directly from the Raspberry Pi itself, leeching power from the 3.3V lines.

## Ground
There's not a lot to say here, connect sensor GND to Pi's GND.
