# TeraHz developer's guide
This document explains how TeraHz works. It's a good starting point for developers
and an interesting read for the curious.

# Hardware
TeraHz was developed on and for the Raspberry Pi 3 Model B+. Compatibility with
other Raspberries can probably be achieved by tweaking the device paths in the
`app.py` file, but isn't confirmed at this point. Theoretically, 3 Model B and
Zero W should work out of the box, but models without Wi-Fi will need an
external Wi-Fi adapter if Wi-Fi functionality is desired.

TeraHz depends on three separate sensor boards:
- AS7265x spectral chipset
- VEML6075 UV sensor
- APDS-9301 lux-meter

The sensors leech power from the GPIO connector, thus eliminating the need for a
separate power supply. The necessary power for the whole system is delivered through
the Raspberry's USB port. This also allows for considerable versatility, as it
enables the resulting device to be either wall-powered or battery-powered.
In a portable configuration, I used a one-cell power bank, which allowed for
about 45 minutes of continuous operation.

## AS7265x chipset
_[Datasheet][1ds] [Buy breakout board][1]_

This chipset supports either I2C or UART. Because transferring large amounts of
data over I2C is rather cumbersome, TeraHz uses AS7265x in UART mode.

This chipset consists of three rather small surface-mounted chips and requires
an EEPROM. To lower the complexity of assembly for the end-user, I recommend
using a breakout board.

The serial UART connection operates at 115200 baud, which seems to be the
standard for most recent embedded peripherals. As with most serial hardware,
the TxD and RxD lines must be crossed over when connecting to the processor.

Communication with the sensor is simple and clear through AT commands. There's
a lot of them, all documented inside the datasheet, but the most important one
is `ATGETCDATA`, which returns the calibrated spectral data from the sensors.

The data is returned in the form of a comma-separated list of floating point
values, ending with a newline. The order is alphabetical, which is __different
from wavelength order__. See the datasheet for more information.

## VEML6075
_[Datasheet][2ds] [Buy breakout board][2]_

This chip communicates through I2C and provides TeraHz with UVA and UVB
irradiance readings. It's not an ideal chip for this task, as it's been marked
End-of-Life by Vishay and it'll have to be replaced with a better one in future
hardware versions of TeraHz.

The chip resides at the I2C address `0x10`. There's not a lot of communication
required: at initialization, the integration time has to be set and after that,
the sensor is ready to go.

16-bit UV values lie in two two-byte registers, `0x07` for UVA and `0x09` for
UVB. For correct result conversion, there are also two correction registers,
UVCOMP_1 and 2, located at `0x0A` and `0x0B`, respectively.

To convert these four values into irradiances, they must be multiplied by
certain constants, somewhat loosely defined in the sensor datasheet. Keep in
mind that the way of computing the "irradiance" is very much experimentally
derived, and even Vishay's tech support doesn't know how exactly to calculate
the irradiance.

## APDS-9301
_[Datasheet][3ds] [Buy breakout board][3]_
This chip measures illuminance in luxes and like the VEML6075, connects through
I2C. Unlike the VEML6075, this chip is very good at its job, providing accurate
and fast results without undefined mathematics or required calibration.

At power-on, it needs to be enabled and the sensor gain set to the high setting,
as the formula for Lux calculation is only defined for that setting. This
initialization is handled by the sensors module.

The lux reading is derived from two channels, descriptively called CH0 and CH1,
residing in respective 16-bit registers at addresses `0xAC` and `0xAE`. After a
successful read of both data registers, the lux value can be derived using the
formula in the sensor's datasheet.



[1]: https://www.tindie.com/products/onehorse/compact-as7265x-spectrometer/
[2]: https://www.sparkfun.com/products/15089
[3]: https://www.sparkfun.com/products/14350
[1ds]: sensor-docs/AS7265x.pdf
[2ds]: sensor-docs/veml6075.pdf
[3ds]: sensor-docs/APDS-9301.pdf
