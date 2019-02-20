import smbus

bus = smbus.SMBus(1)
print(bus.read_word_data(0x10, 0x07))
