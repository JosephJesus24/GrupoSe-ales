<h1 align="center"> Registros de señales EEG </h1>
Horario 3 - Grupo 13 

Laboratorio 5 - Viernes 21/04/2023

## Integrantes

* Joseph Jesus Melgarejo Castillo -joseph.melgarejo@upch.pe
* Gabriel Adolfo Narvaez Montalvo- gabriel.narvaez@upch.pe
* Mauricio Leonardo Ramos Gallegos -  mauricio.ramos@upch.pe
* Diego Alejandro Celis Matias - diego.celis@upch.pe 
* Ricardo Alonso Muñoz Quiroz- ricardo.munoz@upch.pe
---
## Tabla de Contenidos
* [Introducción](#introducción)
* [Marco Teórico](#marco-teórico)
* [Materiales](#materiales)
* [Objetivos](#objetivos)
* [Conexiones usadas](#conexiones-usadas)
* [Video: Señal Analizada](#señales-analizadas)
* [Señales obtenidas](#ploteo-y-explicación-de-las-señales)
* [Archivos de las señales](#archivos-de-eeg-en-open-bci)
* [Ploteo de la señal en Python](#ploteo-en-python)
---     

## Introducción
En el presente laboratorio se realizó la adquisición, visualización y análisis de señales EEG a través del uso de ULTRACORTEX "MARK IV" de 8 canales y del dispositivo de adquisición de señales ,Bitalino.

Para medir señales EEG con Bitalino, se necesitaron dos electrodos colocados en la cabeza del paciente , a la altura de la frente y uno de referencia  en la parte posterior de la oreja. 

<div align="center">
<img src="Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Fotos/conexion_bita1.jpg" alt="Conexion1_Bit" width="200"> 
</div>
<em><p align="center"> Fig1. Conexiones de Bitalino.</p></em>

Y para  la correcta medición del ULTRA CORTEX se requirió de una correcta calibración de los 8 canales ubicados estratégicamente en la cabeza de nuestro compañero ,de acuerdo con el sistema de colocación de electrodos 10/20.

<div align="center">
<img src="Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Fotos/conexion_ultra3.png" alt="Conexion1_Bit" width="200"> 
</div>
<em><p align="center"> Fig2. Conexiones de Ultra Cortex.</p></em>

Cabe resaltar que se realizará una posterior evaluación del registro electroencefalográfico a través de una codificación en python, pudiendo así obtener valores de suma importancia como son la amplitud y frecuencia de las distintas mediciones que se realizaron. Apuntaremos a la  identificación de las ondas alfa y beta, y las señales de interferencia.

## Marco Teórico
    - Breve explicación de las señales que analizaremos y como es su procedimiento de la toma de muestra (Como se usa el EEG, etc)
    - NO OLVIDAR REFERENCIAS

## Materiales
Los materiales usados para el desarrollo de este laboratorio fueron 2 dispositivos capaces de medir señales de biopotenciales EEG, además fue necesario el uso de una laptop para poder registrar las señales tomadas por ambos dispositivos.

<div align="center">

|Materiales |   Descripción      |Referencia         |
|:---       |    :---:           |     :---:         |
| Laptop    | PC portatil        | Cualquier modelo  |
| Bitalino  |Kit de herramientas de prototipado rápido para proyectos de salud y bienestar personal, para adquirir, procesar y visualizar datos biomédicos.|<img src="Grupo_Se%C3%B1ales/Imagenes/BITalino-Board.1_720x.webp" alt="Bitalino" width="500"> <em><p align="center"> Fig3. Bitalino.</p></em>|
|Ultracortex EEG Headset |Dispositivo portátil que se coloca en la cabeza para medir la actividad eléctrica del cerebro y permitir la monitorización y análisis de las ondas cerebrales en tiempo real.   |<img src="Grupo_Se%C3%B1ales/Imagenes/Ultracortex" alt="Bitalino" width="500"> <em><p align="center"> Fig4. Ultracortex EEG Headset.</p></em>|

</div>

<h1 align="center"> Desarrollo del laboratorio </h1>

## Objetivos
    Colocar los objetivos del laboratorio
## Conexiones usadas

Para la toma de muestras, fueron necesario 2 pacientes de prueba para el uso de bitalino y del ultracortex.
Las conexiones que se le hicieron a cada paciente de prueba fueron las siguientes:

<div align="center">

|Paciente de prueba 1| Paciente de Prueba 2|
|:---:               |                :---:|
|   Gabriel Narvaez  |     Diego Celis     |
|<img src="Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Fotos/conexion_bita2.jpg" alt="Conexion1_Bit" width="300"> <em><p align="center"> Fig5. Conexiones señaladas de Bitalino.</p></em> |   <img src="Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Fotos/conexion_ultra2.jpg" width="240"> <em><p align="center"> Fig6. Conexiones de Ultra Cortex según sistema 10/20.</p></em> |
</div>



## Señales Analizadas
    Video de señal mostrando el punto 1,2 y 4 del procedimiento; que se muestre las conexiones electrodos-cuerpo/cabeza y señal ploteada.

    
<h2 align="center"> Toma de regitros con Bitalino </h2>

<div align="center">

<img src="Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Fotos/conexion_bita2.jpg" alt="Conexion1_Bit" width="300">

</div>
<em><p align="center"> Fig2. Conexiones de Bitalino.</p></em>

### Registro 1. Registro de linea basal (30 segundos)
Este registro consiste en la toma de muestra de señal EEG donde el usuario uno permaneció durante 30 segundos en reposo, con los ojos cerrados, sin ninguna distracción y con una respiración normal.

### 2. Registro de ciclo Ojos abiertos - Ojos cerrados
Este registro consiste en la toma de muestra de señal EEG donde el usuario realizó un ciclo de parpadeo 5 veces. Cada momento en el que el usuario permanece con los ojos cerrados o con los ojos abiertos durará 5 segundos.


### 3. Registro de fase de referencia
Registro de reposo, similiar al primer registro, durante 30 segundos.


### 4. Registro cálculo de ejercicios matemáticos
Último registro, nuestro usuario se encargará de resolver una lista de ejercicios matemáticos mentalmente, mirando hacia un solo punto fijo para evitar distracciones.
Esta lista de ejercicios será dictada con la ayuda de una segunda persona que los dirá en voz alta


<h2 align="center"> Toma de regitros con OpenBCI </h2>

<div align="center">

<img src="Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Fotos/conexion_ultra2.jpg" alt="Conexion1_Bit" width="270">

</div>

<em><p align="center"> Fig2. Conexiones de Bitalino.</p></em>

### Registro 1. Registro de linea basal (30 segundos)
Este registro consiste en la toma de muestra de señal EEG donde el usuario uno permaneció durante 30 segundos en reposo, con los ojos cerrados, sin ninguna distracción y con una respiración normal.

### 2. Registro de ciclo Ojos abiertos - Ojos cerrados
Este registro consiste en la toma de muestra de señal EEG donde el usuario realizó un ciclo de parpadeo 5 veces. Cada momento en el que el usuario permanece con los ojos cerrados o con los ojos abiertos durará 5 segundos.

### 3. Registro de fase de referencia
Registro de reposo, similiar al primer registro, durante 30 segundos.

### 4. Registro cálculo de ejercicios matemáticos
Último registro, nuestro usuario se encargará de resolver una lista de ejercicios matemáticos mentalmente, mirando hacia un solo punto fijo para evitar distracciones.
Esta lista de ejercicios será dictada con la ayuda de una segunda persona que los dirá en voz alta.
## Ploteo y Explicación de las señales
    Aquí poner las capturas de los ploteos en Open BCI

<h2 align="center"> Toma de regitros con Bitalino </h2>

### Registro 1: 
<div align="center">
<img src="Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Fotos/Registro1-bit.png" alt="Registro1_Bit" width="1200">
</div>


### Registro 2:
<div align="center">
<img src="Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Fotos/Registro2-bit.png" alt="Registro2_Bit" width="1200">
</div>


### Registro 3: 
<div align="center">
<img src="Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Fotos/Registro3-bit.png" alt="Registro3_Bit" width="1200">
</div>


### Registro 4: 
<div align="center">
<img src="Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Fotos/Registro4-bit.png" alt="Registro4_Bit" width="1200">
</div>




<h2 align="center"> Toma de regitros con Open BCI </h2>

### Registro 1: 
### Registro 2: 
### Registro 3: 
### Registro 4: 

## Archivos de  EEG en Open BCI

<h3 align="center"> Archivos de Bitalino </h3>

1. [Registro 1 - bitalino](Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Se%C3%B1ales/EEG_Bitalino/Registro1.txt)
2. [Registro 2 - bitalino](Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Se%C3%B1ales/EEG_Bitalino/Registro2.txt)
3. [Registro 3 - bitalino](Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Se%C3%B1ales/EEG_Bitalino/Registro3.txt)
4. [Registro 4 - bitalino](Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Se%C3%B1ales/EEG_Bitalino/Registro4.txt)

<h3 align="center"> Archivos de OpenBCI </h3>

1. [Registro 1 - OpenBCI](Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Se%C3%B1ales/EEG_OpenBCI/Registro1_OpenBCI)
2. [Registro 2 - OpenBCI](Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Se%C3%B1ales/EEG_OpenBCI/Registro2_OpenBCI)
3. [Registro 3 - OpenBCI](Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Se%C3%B1ales/EEG_OpenBCI/Registro3_OpenBCI)
4. [Registro 4 - OpenBCI](Grupo_Se%C3%B1ales/Documentaci%C3%B3n/Laboratorio5/Se%C3%B1ales/EEG_OpenBCI/Registro4_OpenBCI)

## Ploteo en Python_
    Agregar un notebook de las señales ploteadas en python.
    Adjuntar un enlace directo al notebook