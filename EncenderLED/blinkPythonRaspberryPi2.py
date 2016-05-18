import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)   # Declaramos que los pines seran llamados como numeros
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT) # GPIO 17 como salida
GPIO.setup(27, GPIO.OUT) # GPIO 27 como salida
GPIO.setup(22, GPIO.OUT) # GPIO 27 como salida 

def blinkLeds():
	print("Inicio")
	for i in range(10):
		leds = raw_input("Introduce 3 digitos en binario para encender o apagar los leds(110,001,111,...):")
		GPIO.output(17, int(leds[0]))  # Encender Pin 17
		GPIO.output(27, int(leds[1]))  # Encender Pin 27
		GPIO.output(22, int(leds[2]))  # Encender Pin 22
		time.sleep(5)	
	print("Fin de programa")
	GPIO.cleanup() #Limpiar los GPIO  


blinkLeds()                           #Llamamos a la funcion blinkLeds para ejecutar el programa

