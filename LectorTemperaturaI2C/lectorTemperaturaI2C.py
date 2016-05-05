# ------------------------------------------------------------------------------------------
#                  Programa en Python para Leer Temperatura Sensor con I2C
# ------------------------------------------------------------------------------------------
#
# Author : Iker Burguera
# Version: v1
# Date   : 05/05/2016 
# Modelo : Raspberry Pi 2 Model B
#-------------------------------------------------------------------------------------------
# Nota   : Leer instrucciones antes de ejecutar el código
#-------------------------------------------------------------------------------------------

import smbus
import time
import datetime

#SMBus(0) - Raspberry Pi Model A
#SMBus(1) - Raspberry Pi Model B

bus = smbus.SMBus(1)

address = 0x34

def temperatura():
    rvalue0 = bus.read_word_data(address,0)
    rvalue1 = (rvalue0 & 0xff00) >> 8
    rvalue2 = rvalue0 & 0x00ff
    rvalue = (((rvalue2 * 256) + rvalue1) >> 4 ) *.0625
    #print rvalue1, rvalue2
    return rvalue

print("Data Logger Temperatura\n")

while True:
    
    #Abrimos fichero de Log para ir guardando 
    f=open('tempdata.txt','a')
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y/%m/%d %H:%M")
    outvalue = temperatura()
    outstring = str(timestamp)+"  "+str(outvalue)+" C "+str(outvalue*1.8+32)+" F"+"\n"
    print outstring
    f.write(outstring)
    f.close()

    #Guardaremos la temperatura cada 30 segundos
    time.sleep(30)
    
