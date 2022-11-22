## STREAMING SERVIDOR CLIENTE CON RTSP
- En este proyecto se establecerá una conexion a traves del protocolo RTSP entre un contenedor cliente con uno servidor.

## Table of Contents
* [Informacion general](#informacion-general)
* [Technologias](#technologias)
* [Instalacion](#instalacion)
* [Uso Basico](#uso-basico)
* [Actualizaciones](#actualizaciones)

## Informacion general
- El protocolo RTSP nos permite generar trafico necesario para transmitir via streaming, en este proyecto se replicará esta accion entre dos contenedores y luego se analizará el trafico para entender a fondo esta comunicacion.

## Technologias
- Docker 
- VLC
- Python3
- Scapy

## Instalacion

**Descargar imagen del servidor**

    $ docker pull aler9/rtsp-simple-server

**Correr el servidor**

    $ docker run --rm -it --network=host aler9/rtsp-simple-server

**Descargar imagen del cliente** 

    $ docker pull galexrt/vlc

**Correr el cliente**

    $ docker \
    run \
    -d \
    -v "$(pwd)":/data \
    --user $(id -u):$(id -g) \
    --publish 8554:8554/udp \
    quay.io/galexrt/vlc:latest 


## Uso Basico

**Publicamos el stream con ffmpeg desde NUESTRO EQUIPO ANFITRION**

    $ ffmpeg -re -stream_loop -1 -i ARCHIVO.mp4 -c copy -f rtsp rtsp://localhost:8554/mystream

Al estar conectado a la network **host**, el stream va a transmitir en `rtsp://localhost:8554/mystream` en los tres dispositivos (maquina anfitriona, cliente y servidor)

Se puede cargar un archivo desde la maquina anfitriona a el docker servidor con el comando `$ docker cp ARCHIVO.mp4 CODIGO_CONTENEDOR_SERVER` o estar en la carpeta del archivo y pasarlo directamente con el comando de arriba (RECOMENDADO) 

**Desde el HOST corremos vlc con el streaming**

    $ vlc rtsp://localhost:8554/mystream

## Actualizaciones

