'''
THORLABS SKELETON CODE
'''

import pyvisa
import time
from datetime import datetime

rm = pyvisa.ResourceManager()
print(rm.list_resources())  # See if PM101 shows up

'''
# Replace with your actual resource string
inst = rm.open_resource('USB0::0x1313::0x8078::PXXXXXXXX::INSTR')

inst.write('*IDN?')
print(inst.read())  # Should print Thorlabs info

while True:
    power = inst.query('MEAS:POW?')  # May differ depending on config
    timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
    print(timestamp, power)
    time.sleep(0.1)
'''