from gpiozero import MCP3008
import time
from numpy import interp
import math
#while(1):

avg=0

for i in range(100):
  adc0=MCP3008(channel=0, device=0)
  adc1=MCP3008(channel=1, device=0)
  added_vals = (adc0.value*1023.0)+(adc1.value*1023.0)
  #print("Weight on Scale: %.2f, %.2f" %(adc0.value*1023, adc1.value*1023))
  print("Added values = %.2f" %added_vals)
  avg += added_vals
  time.sleep(0.01)

avg/=100
print("Average output %.2f" %avg)
print("Mass = %.2f" %(math.exp((avg+2954.8)/717.2)))
   # time.sleep(0.5)
#print("Analog reading = %.2f" %(adc0.value*1023))
#fsrVoltage=interp((adc0.value*1023.0),[0,1023],[0,3300])
#print("Voltage reading in mV = %.2f" %fsrVoltage)
#fsrResistance=(3300-fsrVoltage)*55000.0/fsrVoltage
#print("FSR resistance in ohms =  %.2f" %fsrResistance)
#fsrConductance=(1000000.0/fsrResistance)
#print("Conductance in microMhos =  %.2f" %fsrConductance)

#fsrForce=fsrConductance*9.81/3.54
#print("Force in grams = %.2f" %fsrForce)

#else:
#  fsrForce=(fsrConductance-1000)/30.0
#  print("Force in Newtons = %.2f" %fsrForce)

