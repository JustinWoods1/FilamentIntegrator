from guizero import App, PushButton
def wind_button_press():
  wind_button.hide()
  
app = App()
wind_button = PushButton(app, command=wind_button_press)
app.display()
