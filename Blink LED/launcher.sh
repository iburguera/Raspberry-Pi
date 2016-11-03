#!/bin/sh
# launcher.sh
# 
# 1- Navega al directorio home. 
# 2- Despues desde este directorio navega al directorio a donde esta el script que vamos a ejecutat
# 3- Una vez en el directorio ejecutamos el script y volvemos al directorio home

cd /
cd /home/pi/PythonScript
sudo python pythonBelenRGB.py
cd /