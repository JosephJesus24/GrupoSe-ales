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
<img src="Fotos/conexion_bita1.jpg" alt="Conexion1_Bit" width="200"> 
</div>
<em><p align="center"> Fig1. Conexiones de Bitalino.</p></em>

Y para  la correcta medición del ULTRA CORTEX se requirió de una correcta calibración de los 8 canales ubicados estratégicamente en la cabeza de nuestro compañero ,de acuerdo con el sistema de colocación de electrodos 10/20.

<div align="center">
<img src="Fotos/conexion_ultra3.png" alt="Conexion1_Bit" width="200"> 
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
| Bitalino  |Kit de herramientas de prototipado rápido para proyectos de salud y bienestar personal, para adquirir, procesar y visualizar datos biomédicos.|<img src="../../Imagenes/BITalino-Board.1_720x.webp" alt="Bitalino" width="500"> <em><p align="center"> Fig3. Bitalino.</p></em>|
|Ultracortex EEG Headset |Dispositivo portátil que se coloca en la cabeza para medir la actividad eléctrica del cerebro y permitir la monitorización y análisis de las ondas cerebrales en tiempo real.   |<img src="../../Imagenes/Ultracortex" alt="Bitalino" width="500"> <em><p align="center"> Fig4. Ultracortex EEG Headset.</p></em>|

</div>

<h1 align="center"> Desarrollo del laboratorio </h1>

## Objetivos

* Poder adquirir y analizar señales EEG
* Emplear el software OpenBCI y usar el dispositivo Ultracortex para la toma de señales
* Realizar una segunda medición con el software Bitalino

## Conexiones usadas

Para la toma de muestras, fueron necesario 2 pacientes de prueba para el uso de bitalino y del ultracortex.
Las conexiones que se le hicieron a cada paciente de prueba fueron las siguientes:

<div align="center">

|Paciente de prueba 1| Paciente de Prueba 2|
|:---:               |                :---:|
|   Gabriel Narvaez  |     Diego Celis     |
|<img src="Fotos/conexion_bita2.jpg" alt="Conexion1_Bit" width="300"> <em><p align="center"> Fig5. Conexiones señaladas de Bitalino.</p></em> |   <img src="Fotos/conexion_ultra2.jpg" width="240"> <em><p align="center"> Fig6. Conexiones de Ultra Cortex según sistema 10/20.</p></em> |
</div>


## Señales Analizadas
    
<h2 align="center"> Toma de regitros con Bitalino </h2>

<div align="center">

<img src="Fotos/Registros-bit.jpg" alt="Conexion1_Bit" width="1200">

</div>
<em><p align="center"> Fig7. Registros de ejercicios de Bitalino.</p></em>

### 1. Registro de linea basal (30 segundos)
Este registro consiste en la toma de muestra de señal EEG donde el usuario uno permaneció durante 30 segundos en reposo, con los ojos cerrados, sin ninguna distracción y con una respiración normal.

<div align="center">
    <video src="https://user-images.githubusercontent.com/43487731/233764056-4be7901f-acf7-4714-8eb8-6fc3955dc434.mp4">
</div>
<em><p align="center"> Video1. Ejercicio1 en Bitalino.</p></em>

### 2. Registro de ciclo Ojos abiertos - Ojos cerrados
Este registro consiste en la toma de muestra de señal EEG donde el usuario realizó un ciclo de parpadeo 5 veces. Cada momento en el que el usuario permanece con los ojos cerrados o con los ojos abiertos durará 5 segundos.

<div align="center">
    <video src="https://user-images.githubusercontent.com/43487731/233763534-fe27df17-2006-4958-ab02-ca933bbe7df9.mp4">
</div>
<em><p align="center"> Video2. Ejercicio2 en Bitalino.</p></em>
    
### 3. Registro de fase de referencia
Registro de reposo, similiar al primer registro, durante 30 segundos.

### 4. Registro cálculo de ejercicios matemáticos
Último registro, nuestro usuario se encargará de resolver una lista de ejercicios matemáticos mentalmente, mirando hacia un solo punto fijo para evitar distracciones.
Esta lista de ejercicios será dictada con la ayuda de una segunda persona que los dirá en voz alta

<div align="center">
    <video src="https://user-images.githubusercontent.com/43487731/233763662-c3e35430-3325-47bf-89e0-ea0fde7ad094.mp4">
</div>
<em><p align="center"> Video4. Ejercicio4 en Bitalino.</p></em>
 
<h2 align="center"> Toma de regitros con OpenBCI </h2>

<div align="center">

<img src="Fotos/Registros-OpenBCI.png" alt="Conexion2_Ultra" width="270">
</div>

<em><p align="center"> Fig8. Registros de ejercicios en OpenBCI.</p></em>

Se realizaron los mismos ejercicios de registro de señales con el uso del UltraCortex y el software OpenBCI
### 1. Registro de linea basal (30 segundos)
    
<div align="center">
    <video src="https://user-images.githubusercontent.com/43487731/233763713-8d193e2f-f4f3-4107-8bb1-1f2c6d079269.mp4">
</div>
<em><p align="center"> Video5. Ejercicio1 en OpenBCI.</p></em>
    
### 2. Registro de ciclo Ojos abiertos - Ojos cerrados

<div align="center">
    <video src="https://user-images.githubusercontent.com/43487731/233763726-240f3828-6a1c-4c83-b967-e193d5d2ba87.mp4">
</div>
<em><p align="center"> Video6. Ejercicio2 en OpenBCI.</p></em>
    
### 3. Registro de fase de referencia

<div align="center">
    <video src="https://user-images.githubusercontent.com/43487731/233763735-f9dc003b-4697-4509-9541-d675d6b5caeb.mp4">
</div>
<em><p align="center"> Video7. Ejercicio3 en OpenBCI.</p></em>

### 4. Registro cálculo de ejercicios matemáticos

<div align="center">
    <video src="https://user-images.githubusercontent.com/43487731/233763746-8726fe83-8f0f-4731-b614-441f866f0424.mp4">
</div>
<em><p align="center"> Video8. Ejercicio4 en OpenBCI.</p></em>
    
## Ploteo y Explicación de las señales
    Explicaciones de los ploteos y poner las capturas de los ploteos en Open BCI
    
<h2 align="center"> Toma de regitros con Bitalino </h2>

### Registro 1: 
<div align="center">
<img src="Fotos/Registro1-bit.png" alt="Registro1_Bit" width="1200">
</div>
<em><p align="center"> Fig9. Registro1 en bitalino: Estado basal.</p></em>

### Registro 2:
<div align="center">
<img src="Fotos/Registro2-bit.png" alt="Registro2_Bit" width="1200">
</div>
<em><p align="center"> Fig10. Registro2 en bitalino: OJO ABIERTO/OJO CERRADO.</p></em>

### Registro 3: 
<div align="center">
<img src="Fotos/Registro3-bit.png" alt="Registro3_Bit" width="1200">
</div>
<em><p align="center"> Fig11. Registro3 en bitalino: Estado reposo.</p></em>

### Registro 4: 
<div align="center">
<img src="Fotos/Registro4-bit.png" alt="Registro4_Bit" width="1200">
</div>
<em><p align="center"> Fig12. Registro4 en bitalino: Resolución ejercicios matemáticos.</p></em>



<h2 align="center"> Toma de regitros con Open BCI </h2>

### Registro 1: 
### Registro 2: 
### Registro 3: 
### Registro 4: 

## Archivos de  EEG en Open BCI

<h3 align="center"> Archivos de Bitalino </h3>

1. [Registro 1 - Bitalino](Se%C3%B1ales/EEG_Bitalino/Registro1.txt)
2. [Registro 2 - Bitalino](Se%C3%B1ales/EEG_Bitalino/Registro2.txt)
3. [Registro 3 - Bitalino](Se%C3%B1ales/EEG_Bitalino/Registro3.txt)
4. [Registro 4 - Bitalino](Se%C3%B1ales/EEG_Bitalino/Registro4.txt)

<h3 align="center"> Archivos de OpenBCI </h3>

1. [Registro 1 - OpenBCI](Se%C3%B1ales/EEG_OpenBCI/Registro1_OpenBCI)
2. [Registro 2 - OpenBCI](Se%C3%B1ales/EEG_OpenBCI/Registro2_OpenBCI)
3. [Registro 3 - OpenBCI](Se%C3%B1ales/EEG_OpenBCI/Registro3_OpenBCI)
4. [Registro 4 - OpenBCI](Se%C3%B1ales/EEG_OpenBCI/Registro4_OpenBCI)

## Ploteo en Python_
    Agregar un notebook de las señales ploteadas en python.
    Adjuntar un enlace directo al notebook
