import smbus2

bus = smbus2.SMBus(1)

result = bus.read_byte_data(0x39, 0x8a)
print('LUX Meter ID = {}'.format(result))

result = bus.read_word_data(0x10, 0x0c)
print('UV sensor ID = {}'.format(result))

result = bus.read_word_data(0x39, 0xec)
print('UV sensor ID = {}'.format(result))
