<img src="upch-logo.png" alt=[logo_upch] height="100">

<h1 align="justify"> 
Proposal for classification of SSVEP signals for navigation in patients with motor disabilities with the use of the Ultracortex Mark IV
</h1>

<h3 align="justify"> 
Propuesta de clasificación de señales SSVEP para navegación en pacientes con discapacidad motora con el uso del Ultracortex Mark IV
</h3>

---
Bienvenidos al repositorio del grupo 13

Conoce más [sobre nosotros](<ISB/1. Sobre Nosotros/Sobre Nosotros.md>)

---

<h2 align="justify"> 
Tabla de contenidos:
</h2>

- [Resumen](#resumen)
- [Motivación](#motivación)
- [Principales hallazgos](#principales-hallazgos)
---

## Resumen
<p align="justify"> 
En esta investigación, se exploró la implementación de un sistema de selección de letras basado en SSVEP (Potenciales Evocados Visuales con Respuesta a Estímulos en Frecuencia) para la navegación en línea para pacientes con discapacidad motora utilizando el equipo "Ultracortex Mark IV". Este proyecto tiene el propósito de poder apoyar a los pacientes cuadripléjicos en la búsqueda de poder brindarles más autonomía en sus actividades diarias. Se realizaron pruebas en las que los usuarios se concentraron en la letra "A" mientras se capturaban las señales EEG. Estas señales fueron procesadas y analizadas utilizando técnicas de procesamiento de señales, extracción de características y clasificación. Se aplicaron filtros y técnicas de preprocesamiento para mejorar la calidad de las señales, se extrajeron características relevantes y se utilizó un algoritmo de clasificación para determinar si el usuario estaba mirando la letra "A" o no. Aunque los resultados no fueron los esperados debido a la complejidad del procesamiento de señales EEG, el proyecto sentó las bases para futuras investigaciones en el campo de los sistemas de selección basados en la mirada utilizando SSVEP. Se resalta la importancia del equipo "Ultracortex Mark IV" en la captura precisa de las señales EEG y su potencial aplicación en sistemas de comunicación y control.

</p>

---

## Motivación
<p align="justify"> 
La discapacidad motora es una condición en la cual una persona experimenta limitaciones o dificultades en su capacidad para moverse y controlar sus músculos. Esta discapacidad puede afectar a uno o varios miembros del cuerpo, así como otras áreas relacionadas con el movimiento [1]. 
</p>

<p align="justify">
La cuadriplejia es un tipo de discapacidad motora, esta condición médica en la cual hay una pérdida o disminución de la función motora en los cuatro miembros del cuerpo, incluyendo tanto las extremidades superiores como las inferiores, se debe a una lesión en la médula espinal, generalmente en el nivel cervical, que interrumpe la comunicación entre el cerebro y las partes del cuerpo afectadas.
</p>

<p align="justify">
En el mundo, la incidencia de las lesiones medulares es de 10 a 80 casos por millón de habitantes por año en donde predominan los casos en varones con una relación de 4:1 con respecto a las mujeres y jóvenes de 1:3. La cuadriplejia por lesiones traumáticas, al igual que otras discapacidades motoras, es una discapacidad que no cuenta con datos estadísticos nacionales que reflejen la problemática [2]. Sin embargo, se han encontrado investigaciones las cuales intentan dar una solución a la falta de autonomía en personas con discapacidad motora y con ello ayudarles a no depender de terceros en su actividades diarias y, además, brindarles más confianza y mejorar su autoestima.
</p>

<p align="justify">
En este estudio se propone buscar una solución para la navegación en línea para pacientes cuadripléjicos, con el fin de brindar autonomía con el uso de dispositivos electrónicos, en este caso con el uso de una computadora. 
</p>

---
     
## Principales hallazgos
**La viabilidad de utilizar señales SSVEP para la selección de letras**: Se demostró que es posible capturar y procesar las señales EEG relacionadas con la respuesta SSVEP mientras un usuario mira una letra específica en la pantalla. Esto indica que las señales SSVEP pueden utilizarse como una modalidad de interacción efectiva para la selección de letras.

**Desafíos en el procesamiento de señales EEG**: Se identificaron los desafíos asociados con el procesamiento de las señales EEG capturadas, como el filtrado de ruido, la eliminación de artefactos y la normalización de los datos. Estos desafíos requieren el desarrollo de técnicas de procesamiento de señales adecuadas para obtener una señal EEG limpia y confiable.

**Importancia de la selección de características relevantes**: Se reconoció la importancia de identificar y extraer características relevantes de las señales EEG para mejorar la precisión de la clasificación. Se investigaron diversas técnicas de extracción de características, como la transformada de Fourier y la potencia espectral, para distinguir las respuestas SSVEP en diferentes frecuencias.

**Limitaciones en la precisión de la clasificación**: Aunque se logró clasificar las respuestas SSVEP en cierta medida, los resultados no alcanzaron la precisión esperada. Esto sugiere que se necesitan investigaciones adicionales y mejoras en los algoritmos de clasificación para lograr una mayor precisión en la identificación de la letra seleccionada por el usuario.

<div align="center">
<img src="image.png" alt="Canales EEG" width="500">

*fig 1. Error de filtrado de las señales EEG extraídas de la muestra A.*
</div>



---

[1] J. C. Granados-Carrera and J. C. Granados-Carrera, "Efecto de la rehabilitación en la calidad de vida de personas con lesión medular," Anales de La Facultad de Medicina, vol. 81, no. 1, pp. 6-13, 2020. [Online]. Available: https://doi.org/10.15381/ANALES.V81I1.16852 

[2] César, J., & Carrera, G. (2020). ARTÍCULO ORIGINAL 6 An Fac med. 81(1), 6–13. https://doi.org/10.15381/anales.v81i1.16852 

---

<h3 align="justify"> 
Aquí encontrará los enlaces a los códigos utilizados durante el proyecto
</h3>

- [Interfaz gráfica](<Software/Codigos py/Interfaz_GráficaSSVEP.py>)
- [Filtrado de las señales](<Software/Codigos py/Filter_channels.ipynb>)
- [Muestras EEG recopiladas](Software/Se%C3%B1ales)

<h3 align="justify"> 
Materiales
</h3>

- [Software](Software/README.md)
- [Hardware](Hardware/README.md)

<h3 align="justify"> 
Docentes del curso
</h3>

- Lewis de la Cruz - umbert.de.la.cruz@upch.pe
- Moises Meza - moises.meza@upch.pe
- José Alonso Cáceres - jo.alonsok@gmail.com

