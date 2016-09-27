import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)   # Declaramos que los pines seran llamados como numeros
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN)  # GPIO  7 como entrada
GPIO.setup(17, GPIO.IN) # GPIO 17 como entrada
GPIO.setup(27, GPIO.IN) # GPIO 27 como entrada
GPIO.setup(22, GPIO.IN) # GPIO 22 como entrada

pathVideos = "/home/pi/VideoHD/Belen"                                   # Directorio donde se encuentran los videos en HD

def reproducirVideos(nameVideo):
	command1 = "sudo killall -s 9 omxplayer.bin"
	os.system(command1)
	command2 = "omxplayer -p -o hdmi %s/%s.mp4 &" % (pathVideos,nameVideo)
	os.system(command2)
        print "Reproduciendo el Video: %s " % nameVideo

def programaPrincipal():
        print("Inicio")

        while True:
                if (GPIO.input(4)):
                        print("Iniciando Video: AMANECER")
                        reproducirVideos("amanecer")
                elif (GPIO.input(17)):
                        print("Iniciando Video: DIA")
                        reproducirVideos("dia")
                elif (GPIO.input(27)):
                        print("Iniciando Video: ATARDECER")
                        reproducirVideos("atardecer")
                elif (GPIO.input(22)):
                        print("Iniciando Video: ANOCHECER")
                        reproducirVideos("anochecer")
                else:
                        pass
        print("Fin de programa")
        GPIO.cleanup() #Limpiar los GPIO  


programaPrincipal()                           #Llamamos a la funcion programaPrincipal para ejecutar el programa

