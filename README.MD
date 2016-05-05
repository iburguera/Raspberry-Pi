##Programa en Python para Leer Temperatura Sensor con I2C
-------------------------------------------------------------------------------------------

Es importante seguir todos los pasos en el orden en el que se muestran a continuación. 

###Habilitar el protocolo I2C en la placa Raspberry Pi

1. Nos conectamos a la Raspberry Pi usando SSH y ejecutamos el siguiente comando para habilitar el i2c en la placa
2. sudo nano /etc/modprobe.d/raspi-blacklist.conf
3. Dejamos el fichero tal y como está a continuación, incluyendo los hashes '#'
```python
   #blacklist spi and i2c by default (many users don't need them)

     blacklist spi-bcm2708
   #blacklist i2c-bcm2708
```
------------------------------------------------------------------------------------------
###Modificamos el fichero config.txt para indicarle que vamos a activar el i2C en la placa Raspberry Pi
------------------------------------------------------------------------------------------
1. Ejecutamos el comando    sudo nano /boot/config.txt
2. Agregamos los siguientes código a al fichero

```
    dtparam=i2c1=on
    dtparam=i2c_arm=on
```
------------------------------------------------------------------------------------------
###Indicamos que queremos cargar los modulos I2C en el boot de arranque de  la placa Raspberry Pi
------------------------------------------------------------------------------------------
1. Ejecutamos el comando  sudo nano /etc/modules
2. Agregamos los siguientes código a al fichero:    
```
    i2c-bcm2708
    i2c-dev
```

------------------------------------------------------------------------------------------
###Instalamos las Herramientas I2C
------------------------------------------------------------------------------------------
``` 
    sudo apt-get install i2c-tools
    sudo apt-get install python-smbus
```
------------------------------------------------------------------------------------------
###Agregamos usuario pi al i2c 
------------------------------------------------------------------------------------------
```
    sudo adduser pi i2c
```
------------------------------------------------------------------------------------------
###Comando para detectar los dispositivos I2C Conectados
------------------------------------------------------------------------------------------
1. Utilizamos el siguiente comando para saber en que dirección debemos leer el registro
```
     Modelo A -> i2cdetect -y0
     Modelo B -> i2cdetect -y1 
```

       Si el resultado es 34 la dirección sera = 0x34 
 ------------------------------------------------------------------------------------------ 
