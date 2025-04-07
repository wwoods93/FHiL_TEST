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
inst.write(':SYST:LANG ENGLISH\n')
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

# DHO924S command testing


# inst.write(':RUN\n')    # start running the oscilloscope (=RUN button)
# inst.write(':STOP\n')   # stop running the oscilloscope (=STOP button)


# inst.write(':SING\n')   # performs a single trigger (=SIGNLE button)
# inst.write(':CLE\n') # clear all waveforms (=CLEAR button)
# inst.write(':AUT\n')  # run in auto mode (=AUTO button)
# inst.write(':TFOR\n')  # run in single trigger mode (=SINGLE button)

# inst.write(':AUT:PEAK 0\n')  # peak to peak priority ensures full signal diplayed in case of large offset
# response = inst.query(':AUT:PEAK?\n') # check if peak to peak priority mode is set
# response = inst.query(':AUT:OPEN?\n') # sets or queries whether to only test enabled channel when performing AUTO run

# response = inst.query(':AUT:OVER?\n') # waveform overlap
# response = inst.query(':AUT:KEEP?\n') # keep coupling for subsequent AUTO operations (otherwise default is DC coupling)
# response = inst.query(':AUT:LOCK?\n') # ON locks AUTO key, disables AUTO function. OFF unlocks AUTO key, enables AUTO function

# inst.write(':ACQ:AVER 16\n')  # set the number of samples taken in average acquisition mode
# response = inst.query(':ACQ:AVER?\n')     # query the sampling rate for average acquisition mode

# response = inst.query(':ACQ:TYPE?\n') # queries current acquistion type
# inst.write(':ACQ:TYPE AVER\n')  # set acquisition type to average

# response = inst.query(':ACQ:SRAT?\n')  # returns sampling rate in scientific notation
# inst.write(':ACQ:ULTRA:MODE ADJ\n')
# response = inst.query(':ACQ:ULTR:MODE?\n')

# inst.write(':ACQ:ULTRA:TIM 0.1\n')
# response = inst.query(':ACQ:ULTR:TIM?\n')
# inst.write(':CHAN1:BWL ON\n')   # Enable bandwidth limit for channel 1  
# response = inst.query(':CHAN1:BWL?\n')  # Query the bandwidth limit for channel 1

# inst.write(':CHAN1:COUP AC\n')  # AC coupling = DC blocked, DC coupling = none blocked, GND = all blocked
# response = inst.query(':CHAN1:COUP?\n')

# inst.write(':CHAN1:DISP ON\n')  # enable channel 1
# response = inst.query(':CHAN1:DISP?\n')  # Query the display status for channel 

# inst.write(':CHAN1:OFFS 0.0\n')  # Set the vertical offset for channel 1 to 0.0 V
# response = inst.query(':CHAN1:OFFS?\n')

# inst.write(':CHAN1:SCAL 0.5\n') # set vertical scale to 0.5 V/div
# response = inst.query(':CHAN1:SCAL?\n')  # Query the vertical scale for channel 1

# inst.write(':CHAN1:PROB 10\n')  # Set the probe attenuation factor for channel 1 to 10
# response = inst.query(':CHAN1:PROB?\n')

# inst.write(':CHAN1:UNIT VOLT\n')
# response = inst.query(':CHAN1:UNIT?\n')  # Query the unit for channel 1

# inst.write(':CHAN1:POS 5.0\n')  # Set the vertical offset for channel 1 to 5.0 divisions
# response = inst.query(':CHAN1:POS?\n')  # Query the vertical offset for channel 1



# inst.write(':MEAS:COUN:ENAB 1\n')  # Enable counter function
# inst.write(':MEAS:COUN:SOUR CHAN1\n')  # Set the counter source to Channel 1
# response = inst.query(':MEAS:COUN:VAL?\n')  # Query the current counter value

# response = inst.query(':MEAS:ITEM? VMAX,CHAN1\n')  # Measure the maximum voltage on Channel 1

# response = inst.query(':MEAS:ITEM? VMIN,CHAN1\n')  # Measure the minimum voltage on Channel 1

# inst.write(':MEAS:STAT:ITEM VPP,CHAN1\n')  # Set the measurement item to VPP (peak-to-peak voltage) for Channel 1
# response = inst.query(':MEAS:STAT:ITEM? MAX,VPP\n') 

# response = inst.query(':SYST:ERR?\n')  # Query the system error queue

# respomse = inst.query(':SYST:VERS?\n')  # Query the system version

# response = inst.query(':TRIG:MODE?\n')  # Query the current trigger mode

# response = inst.query(':TRIG:COUP?\n')  # Set the trigger mode to AUTO

# response = inst.query(':TRIG:STAT?\n')
# response = inst.query(':TRIG:SWE?\n')  # Query the current trigger mode

# inst.write(':TRIG:NREJ ON\n')       # turn on noise rejection
# response = inst.query(':TRIG:NREJ?\n')  # query nnoise rejection setting

# response = inst.query(':TRIG:EDGE:SOUR?\n')
# response = inst.query(':TRIG:EDGE:LEV?\n')  # Query the current trigger level
# response = inst.query(':TRIG:EDGE:SLOP?\n')

# response = inst.query(':TRIG:PULS:SOUR?\n')  # Query the current pulse source

# response = inst.query(':TRIG:PULS:POL?\n')  # Query the current pulse polarity

# response = inst.query(':TRIG:PULS:WHEN?\n')  # Query the current pulse trigger condition

print(response)

inst.close()
