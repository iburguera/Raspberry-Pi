#!/bin/sh
# launcher.sh
# 
# 1- Ejecutamos ese comando para que no muestre el prompt de login al inicio
# 2- Navega al directorio home. 
# 3- Despues desde este directorio navega al directorio a donde esta el script que vamos a ejecutat
# 4- Una vez en el directorio ejecutamos el script y volvemos al directorio home

sudo systemctl disable getty@tty1.service
cd /
cd /home/pi/PythonScript
sudo python pythonReproducirVideos.py
cd /
