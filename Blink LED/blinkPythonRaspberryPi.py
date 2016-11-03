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
		GPIO.output(17, True)  # Encender Pin 17
		time.sleep(1)
		GPIO.output(17, False) # Encender Pin 17
		time.sleep(1)
		GPIO.output(27, True)  # Encender Pin 27
		time.sleep(1)
		GPIO.output(27, False) # Encender Pin 27
		time.sleep(1)
		GPIO.output(22, True)  # Encender Pin 22
		time.sleep(1)
		GPIO.output(22, False) # Encender Pin 22
		time.sleep(1)		
	print("Fin de programa")
	GPIO.cleanup() #Limpiar los GPIO  
 
blinkLeds()                           #Llamamos a la funcion blinkLeds para ejecutar el programa



