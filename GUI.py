from guizero import App,ButtonGroup,Box,Text,TitleBox,TextBox,Picture,PushButton
from gpiozero import MCP3008
import RPi.GPIO as GPIO
from time import sleep
import math


#servo_pinL = 18
#servo_pinR = 22
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(servo_pinL, GPIO.OUT)
#GPIO.setup(servo_pinR, GPIO.OUT)
#pwmL=GPIO.PWM(servo_pinL,50)
#pwmR=GPIO.PWM(servo_pinR,50)

###################################FUNCTIONS
def measure_button_press():
  measure_button.hide()
 # guide_button.hide()
  title.value="MEASUREMENT MENU"
  spool_title.show()
  spool_model.show()
  get_weight_button.show()
  mass_title.show()
  mass_measurement.show()
  back_button.show()

#def fgs_button_press():
 # guide_button.hide()
 # measure_button.hide()
 # title.value="FILAMENT GUIDANCE SYSTEM MENU"
 # guidance_box.show()
 # fgs_on_button.show()
#  fgs_off_button.show()
 # back_button.show()

#def fgs_control():
 #   pwmL.start(0)
    #pwmR.start(0)
  #  dc = 0
  #  speed=0.002
   # i=0

   # for i in range (1,100,1):
   #   sleep(1) 
   #   print("Enter while loop")
   #   for dc in range(1,100,1):
   #     pwmL.ChangeDutyCycle(10.3+(dc*0.0015))
   #    # pwmR.ChangeDutyCycle(5.3-(dc*0.0015))
   #     sleep(speed)
   #   for dc in range(100,1,-1):
   #     pwmL.ChangeDutyCycle(10.3+(dc*0.0015))
        #pwmR.ChangeDutyCycle(5.3-(dc*0.0015))
   #     sleep(speed)
   # pwmL.stop()
   # #pwmR.stop()

def chosen_spool():
  if spool_model.value   == "ESSENTIUM(Notch)":
    spool_selected.value = 325.46
  elif spool_model.value == "ESSENTIUM(Hole)":
    spool_selected.value = 398.66
  elif spool_model.value == "HATCHBOX":
    spool_selected.value = 297.68
  elif spool_model.value == "MAKERBOT":
    spool_selected.value = 322.08

def get_weight():
  print("READING FORCE RESISTOR VALUE")
  print("PERFORMING COMPUTATION")
#found in FR
  avg=0
  for i in range(100):
    adc0=MCP3008(channel=0, device=0)
    adc1=MCP3008(channel=1, device=0)
    added_vals=(adc0.value*1023.0)+(adc1.value*1023.0)
    avg+=added_vals
    sleep(0.01)

  avg/=100
  mass_measurement.value=round(math.exp((avg+2954.8)/717.2)-192-float(spool_selected.value),2)
  #mass_measurement.value=round((adc0.value*1023+adc1.value*1023)-float(spool_selected.value),2)
  #mass_measurement.value=float(mass_measurement.value)+20+float(spool_selected.value)

def back_button_press():
  title.value="WELCOME, AML ASISTANT"
  measure_button.show()
 # guide_button.show()
  back_button.hide()
  spool_title.hide()
  mass_title.hide()
  get_weight_button.hide()
 # guidance_box.hide()
  mass_measurement.value = 0
 # pwmL.stop()
 # pwmR.stop()
#MAIN
	#main menu
app = App(title="FILAMENT INTEGRATOR",layout="grid")
title = Text(app, text="WELCOME, AML ASSISTANT!",grid=[1,1])
bu_logo = Picture(app,image="logo_Baylor_University.png",grid=[0,0])
measure_button = PushButton(app,text="MEASURE FUNCTION",pady=10,width=20,height=6,grid=[1,3],\
	command=measure_button_press)
#guide_button   = PushButton(app,text="GUIDANCE FUNCTION",pady=10,width=20,height=6,grid=[1,5],\
	#command=fgs_button_press)
#exit_button = PushButton(app, text="EXIT",grid=[0,6], command=servo_close)

	#measure menu
spool_title = TitleBox(app,text="CHOOSE SPOOL",grid=[1,2],visible=False)

spool_model = ButtonGroup(spool_title,\
	options=["ESSENTIUM(Notch)","ESSENTIUM(Hole)","HATCHBOX", "MAKERBOT"],\
	command=chosen_spool,visible=True)
spool_selected = Text(spool_title, text = "325.46",visible=False)

get_weight_button = PushButton(app,text="MEASURE",width=20,height=6,\
	grid=[1,5],command=get_weight,visible=False)
get_weight_button.bg=(0,255,0)

mass_title = TitleBox(app,text="MASS OF FILAMENT",grid=[2,2],visible=False)
mass_measurement = Text(mass_title,text=0,visible=False)
back_button = PushButton(app,text="BACK", grid=[0,5],visible=False,command=back_button_press)

	#guidance menu
#guidance_box = Box(app,layout="grid",grid=[1,2],visible=False)
#fgs_on_button = PushButton(guidance_box,text="ON",width=15,grid=[0,0],\
#	command=fgs_control,visible=False)
#fgs_on_button.bg=(0,255,0)
#fgs_on_button.text_size=18

#fgs_off_button = PushButton(guidance_box,text="OFF",width=15,grid=[0,2],\
#	command=fgs_control,visible=False)
#fgs_off_button.bg=(255,0,0)
#fgs_off_button.text_size=18

app.set_full_screen()
app.display()
