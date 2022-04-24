from guizero import App,ButtonGroup,Box,Text,TitleBox,TextBox,Picture,PushButton

#FUNCTIONS
def measure_button_press():
  measure_button.hide()
  guide_button.hide()
  title.value="MEASUREMENT MENU"
  spool_title.show()
  spool_model.show()
  get_weight_button.show()
  mass_title.show()
  mass_measurement.show()
  back_button.show()

def fgs_button_press():
  guide_button.hide()
  measure_button.hide()
  title.value="FILAMENT GUIDANCE SYSTEM MENU"
  guidance_box.show()
  duty_plus_button.show()
  speed_title.show()
  speed_value.show()
  duty_minus_button.show()
  back_button.show()

def chosen_spool():
  if spool_model.value == "ESSENTIUM":
    spool_selected.value = 75
  elif spool_model.value == "HATCHBOX":
    spool_selected.value = 85
  elif spool_model.value == "MAKERBOT":
    spool_selected.value = 95

def get_weight():
  print("READING FORCE RESISTOR VALUE")
  print("PERFORMING COMPUTATION")
  mass_measurement.value = int(mass_measurement.value) + 20 +int(spool_selected.value)

def duty_plus():
  print("INCREASE DUTY")
  speed_value.value=int(speed_value.value)+1

def duty_minus():
  print("DECREASE DUTY")
  speed_value.value=int(speed_value.value)-1

def back_button_press():
  title.value="WELCOME, AML ASISTANT"
  measure_button.show()
  guide_button.show()
  back_button.hide()
  spool_title.hide()
  mass_title.hide()
  get_weight_button.hide()
  guidance_box.hide()

#MAIN
	#main menu
app = App(title="FILAMENT INTEGRATOR",layout="grid")
title = Text(app, text="WELCOME, AML ASSISTANT!",grid=[1,1])
bu_logo = Picture(app,image="logo_Baylor_University.png",grid=[0,0])
measure_button = PushButton(app,text="MEASURE FUNCTION",pady=10,width=20,height=6,grid=[1,3],\
	command=measure_button_press)
guide_button   = PushButton(app,text="GUIDANCE FUNCTION",pady=10,width=20,height=6,grid=[1,5],\
	command=fgs_button_press)

	#measure menu
spool_title = TitleBox(app,text="CHOOSE SPOOL",grid=[1,2],visible=False)

spool_model = ButtonGroup(spool_title, options=["ESSENTIUM", "HATCHBOX", "MAKERBOT"],\
	command=chosen_spool,visible=True)
spool_selected = Text(spool_title, text = 0)

get_weight_button = PushButton(app,text="MEASURE",width=20,height=6,\
	grid=[1,5],command=get_weight,visible=False)
get_weight_button.bg=(0,255,0)

mass_title = TitleBox(app,text="MASS OF FILAMENT",grid=[2,2],visible=False)
mass_measurement = Text(mass_title,text=0,visible=False)
back_button = PushButton(app,text="BACK", grid=[0,5],visible=False,command=back_button_press)

	#guidance menu
guidance_box = Box(app,layout="grid",grid=[1,2],visible=False)
duty_plus_button = PushButton(guidance_box,text="+",width=15,grid=[0,0],\
	command=duty_plus,visible=False)
duty_plus_button.bg=(0,255,0)
duty_plus_button.text_size=18

speed_title = TitleBox(guidance_box,"DUTY CYCLE",grid=[0,1],visible=False)
speed_value = Text(speed_title, text=0,visible=False)

duty_minus_button = PushButton(guidance_box,text="-",width=15,grid=[0,2],\
	command=duty_minus,visible=False)
duty_minus_button.bg=(255,0,0)
duty_minus_button.text_size=18

app.set_full_screen()
app.display()
