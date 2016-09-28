### SCRIPT PYTHON PARA REPRODUCIR VIDEOS EN RASPBERRY PI ###



Este mini proyecto consiste en reproducir videos almacenados en la **SD** de la **Raspberry Pi** al pulsar los botones conectados a la placa. Tenemos que instalar el reproductor **OMXPlayer** en la **Raspberry Pi**.

El Bash Script **launcher.sh** se ejecuta al inicio de la Raspberry Pi a traves de una tarea **cron**. 
Este script en bash se encarga de ejecutar otro script en python **pythonReproducirVideos.py**. Este script se encargará de recopilar informacion de los pines **GPIO** de la Raspberry Pi.

```
sudo apt-get install omxplayer      
```


El objetivo de este proyecto consiste en **reproducir videos** de las diferentes **fases** del día **(Amanecer, Día, Atardecer, Anochecer)** al **pulsar el boton** correspondiente de cada acción.

El proyecto final irá **sin botones** ya que la señal de **Trigger** nos la dará otro equipo. 

Los **botones** están aquí para **simular** ese botón de Trigger

Para ello tenemos varios ficheros:

1. Video **AMANECER**
  - Este video se reproducirá al pulsar el boton **GPIO 4** - amanecer.mp4
2. Video **DIA**
  - Este video se reproducirá al pulsar el boton **GPIO 17** - dia.mp4
3. Video **ATARDECER**
  - Este video se reproducirá al pulsar el boton **GPIO 27** - atardecer.mp4
4. Video **ANOCHECER**
  - Este video se reproducirá al pulsar el boton **GPIO 27** - anochecer.mp4
  
Al pulsar cualquiera de estos botones, le ordenamos a la placa que reproduzca el video asignado.

Para ello tenemos que conectar el cable **HDMI** de la placa al **monitor** o **Televisor**.

## Eliminar letras de log en la carga de la Raspberry Pi ##

1 - Raspberry Pi Login sin texto de carga modificar el fichero cmdline.txt:
     
```bash
     sudo nano /boot/cmdline.txt
```
Resultado:

```bash
      dwc_otg.lpm_enable=0 console=serial0,115200 console=tty3 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait loglevel=3 quit logo.nologo vt.global_cursor_default=0
```

2- Deshabitar el prompt para que no aparezca el Login (SSH sigue funcionando correctamente)

```bash
       sudo systemctl disable getty@tty1.service   # Disables tty1 service on the screen  <- Utilizamos este comando solo
     # sudo systemctl enable getty@tty1.service    # Enables  tty1 service on the screen
 ```

Ver el codigo para entender mejor el funcionamiento del programa.
