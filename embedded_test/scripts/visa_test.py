import pyvisa
print(pyvisa.__version__)

# from gpib_ctypes import gpib
# print(gpib.__version__)


# Create a resource manager using the Python backend
rm = pyvisa.ResourceManager()
# List available instruments
print(rm.list_resources())
# Open a specific instrument resource (replace with your device details)

# inst = rm.open_resource('TCPIP::192.168.1.100::INSTR')
# # Send a command to the instrument
# response = inst.query("*IDN?")
# print(response)

# inst.write('MEAS:VOLT:DC?\n')
# voltage = inst.read()
# print(f"Voltage: {voltage}")
# inst.close()

# inst = rm.open_resource('TCPIP::192.168.1.101::INSTR')
# # Send a command to the instrument
# response = inst.query("*IDN?")
# print(response)

# inst.write('MEAS:VOLT:DC?\n')
# voltage = inst.read()
# print(f"Voltage: {voltage}")
# inst.close()


inst = rm.open_resource('TCPIP::192.168.1.100::INSTR')
# Send a command to the instrument
response = inst.query("*IDN?")
print(response)

# failed
# response = inst.query(':AUT:ENA 1\n')

# not tried
# :TFOR

# inst.query('MEAS:VOLT:DC?\n')
# voltage = inst.read()
# print(f"Voltage: {voltage}")

# inst.write(':RUN\n')
# inst.write(':STOP\n')


# inst.write(':SING\n')
# inst.write(':CLE\n')
# inst.write(':AUT\n')

# response = inst.query(':AUT:PEAK?\n')
# response = inst.query(':AUT:OPEN?\n')
# response = inst.query(':AUT:OVER?\n')
# response = inst.query(':AUT:KEEP?\n')
# response = inst.query(':AUT:LOCK?\n')

# inst.write(':ACQ:AVER 16\n')
# response = inst.query(':ACQ:AVER?\n')
# response = inst.query(':ACQ:SRAT?\n')
# inst.write(':ACQ:ULTRA:MODE ADJ\n')
# response = inst.query(':ACQ:ULTR:MODE?\n')

inst.write(':ACQ:ULTRA:TIM 0.1\n')
response = inst.query(':ACQ:ULTR:TIM?\n')
print(response)

inst.close()