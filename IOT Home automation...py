import time
import requests
import temperature # temperature sensor
import RPi.GPIO as GPIO
from ubidots import ApiClient

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)



api = ApiClient(token= 'A1E-WLuKlvx6mrCQVf22RF45pLuVlE0yrY')

var1 = api.get_variable("5c5dee81c03f971822e82a47")
var2 = api.get_variable("5c5dee90c03f971822e82a57")
var3 = api.get_variable("5c5dcfacc03f9779d3ecf28c")



while True:
    last_value = var1.get_values(1)
    
    # first relay control s1
    if last_value[0]['value']:
        GPIO.output(35, 1)
        time.sleep(1)
    else:
        GPIO.output(35, 0)
        time.sleep(1)
        
    last_value = var2.get_values(1)
    #print(print (last_value[0]['value']))
    #second relay control s1
    if last_value[0]['value']:
        GPIO.output(37, 1)
        time.sleep(1)
    else:
        GPIO.output(37, 0)
        time.sleep(1)     
    
           
    
    #temperature sensor pin 7 board
    x =temperature.temp()
    response = var3.save_value({"value": x}) 
    print (x)
    #print (y)
