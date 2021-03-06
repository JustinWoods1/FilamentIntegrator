
import RPi.GPIO as GPIO
from time import sleep

## add your servo BOARD PIN number ##
servo_pinL = 18
servo_pinR = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pinR, GPIO.OUT)
GPIO.setup(servo_pinL, GPIO.OUT)
pwmL=GPIO.PWM(servo_pinL, 50)
pwmR=GPIO.PWM(servo_pinR, 50)

pwmL.start(0)
pwmR.start(0)

dc=0
speed=0.002


try:
  while True:
    i=3

 #   for dc in range(9,11,1):
#      print("i= %d" %i)
    for dc in range(1,100,1):
      pwmL.ChangeDutyCycle(10.3+(dc*0.0015))
      pwmR.ChangeDutyCycle(5-(dc*0.0015))
     # pwmR.ChangeDutyCycle((dc-i))
     # pwmL.ChangeDutyCycle(dc)
     # i+=2
      sleep(speed)
 #     print("L=%d, R=%d" %(dc,(dc-i)))

  #  for dc in range(11,9,-1):
  #    print("i=%d" %i)
    for dc in range(100,1,-1):
      pwmL.ChangeDutyCycle(10.3+(dc*0.0015))
      pwmR.ChangeDutyCycle(5-(dc*0.0015))
     #pwmR.ChangeDutyCycle((dc-i))
     # pwmL.ChangeDutyCycle(dc)
     # i-=2
      sleep(speed)
 #     print("L=%d, R=%d" %(dc, (dc-i)))

except KeyboardInterupt:
  print("Ctl C pressed - ending program")
pwmR.stop()
pwmL.stop()
GPIO.cleanup()
