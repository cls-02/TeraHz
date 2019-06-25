# TeraHz developer's guide
This document explains how TeraHz works. It's a good starting point for developers
and an interesting read for the curious.

# Hardware
TeraHz was developed on and for the Raspberry Pi 3 Model B+. Compatibility with
other Raspberries can probably be achieved by tweaking the device paths in the
`app.py` file, but isn't confirmed at this point. Theoretically, 3 Model B and
Zero W should work out of the box, but models without Wi-Fi will need an
external Wi-Fi adapter if Wi-Fi functionality is desired. The practicality of
compiling Python on the first generation of Raspberry Pis is also very
questionable.

Sensors required for operation are (links are breakout board shops):
+ [__AS7265x__](https://www.tindie.com/products/onehorse/compact-as7265x-spectrometer/)
+ [__VEML6075__](https://www.sparkfun.com/products/15089)
+ [__APDS-9301__](https://www.sparkfun.com/products/14350)

They provide the spectrometry data, UV data and illuminance data, respectively.
They all support I2C, AS7265x supports UART in addition.

The sensors leech power from the GPIO connector, thus eliminating the need for a
separate power supply. The necessary power for the whole system is delivered through
the Raspberry's USB port. This also allows for considerable versatility, as it
enables the resulting device to be either wall-powered or battery-powered.
In a portable configuration, I used a one-cell power bank, which allowed for
about 45 minutes of continuous operation.
