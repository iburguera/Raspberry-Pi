### PROGRAMA PYTHON PARA REPRODUCIR VIDEOS EN RASPBERRY PI ###

Este mini proyecto consiste en reproducir videos almacenados en la **SD** de la **Rapsberry Pi** al pulsar los botones conectados a la placa.

El proyecto consiste en **reproducir videos** de las diferentes **fases** del día **(Amanecer, Día, Atardecer, Anochecer)** al **pulsar el boton** correspondiente de cada acción.

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

Ver el codigo para entender mejor el funcionamiento del programa.
