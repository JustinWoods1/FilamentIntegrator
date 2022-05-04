

import spidev
import time
from MCP3008 import MCP3008

#adc1 = MCP3008()
#adc2 = MCP3008()
#value1 = adc1.read(channel=0)
#value2 = adc2.read(channel=1)
#print("Applied voltages %.2f, %.2f" %(value1/1024.0*3.3, value2/1024.0 * 3.3))

#Define Variables
delay=0.5
pad1_channel=0
pad2_channel=1
#Create SPI
spi1=spidev.SpiDev()
spi1.open(0,0)
spi1.max_speed_hz=1350000

spi2=spidev.SpiDev()
spi2.open(0,1)
spi2.max_speed_hz=1350000

def readadc(adcnum):
  #read SPI data from the MCP3008, 8 channels in total
  if adcnum >  7 or adcnum < 0:
    return -1
  r=spi1.xfer2([1,8+adcnum<<4,0])
  data=((r[1]&3) << 8)+r[2]
  return data

try:
  while True:
    pad1_value=readadc(pad1_channel)
    pad2_value=readadc(pad2_channel)
    print("--------------------")
    print("Pressure Pads Value: %d, %d" %(pad1_value/1023.0*3.3,pad2_value/1023.0*3.3))
    time.sleep(delay)
except KeyboardInterrupt:
    pass
