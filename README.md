# TFM_Industriales_UC3M


## _" Generación realista de entornos domésticos en simulación para robots móviles asistenciales"_

### Máster en Ingeniería Industrial - Universidad Carlos III de Madrid

#### DOCUMENTACIÓN DEL PROYECTO EN LA PESTAÑA 'WIKI':

[https://github.com/Noelia-vera/TFG-Noelia-Fernandez-Talavera/wiki](https://github.com/Noelia-vera/TFG-Noelia-Fernandez-Talavera/wiki)

</p>

***

#### ORGANIZACIÓN DE CARPETAS:

* **dataset_mixto:** Códigos para subir a la placa Arduino que controla el movimiento del robot y la toma de datos de los sensores.
* **dataset_simulado:**  Códigos para ejectar en la Raspberry de manejo del robot y subida de datos a la BBDD.
* **resultados:** códigos para ejecutar en Unity para el movimiento manual, automático y evacuación del robot.
* **test_real:** Diseño en AutoCAD de todos los componentes para la simulación del robot en Unity, imágenes del robot real y de las partes de la torre de bomberos para la simulación (primera planta y sótano).
* **albumentation.py:** Planos de las cotas y las vistas de los componentes del robot para la simulación del robot en Unity.


***


#### RESUMEN

Este Trabajo de Fin de Grado consiste en el desarrollo he implementación de un agente autónomo terrestre, capaz de monitorizar el entorno gracias a la tecnología Ultra -Wide Band para la localización de interiores. Posee tres modos de movimiento: de forma manual controlada por teclado, automática realizando un recorrido definido por el usuario, y evacuación creando una ruta alternativa hacia la salida para posibles víctimas. Además, lleva instalados unos sensores de ultrasonidos para esquivar obstáculos he identificar la posición exacta de cada amenaza. 

También, se han incorporado sensores ambientales para monitorizar el entorno de intervención. Los parámetros selecionados son temperatura, CO2, % de humedad relativa, concentración bruta de H2, compuestos volátiles orgánicos y etanol. Son almacenados en una base de datos y representados en una plataforma visual en tiempo real llamada Grafana. De esta forma se puede evaluar la calidad del aire a lo largo de la intervención para garantizar la seguridad de los equipos de emergencias.

Por último, se ha creado una simulación del agente autónomo y del entorno de intervención, que presentan las mismas características que los real. Por un lado, se ha  programado el entorno incorporando fuego, obstáculos y personas; por otro lado se ha programa el comportamiento del autómata creando un modo manual, un modo automático que hace un recorrido similar al que se realiza en las pruebas y un modo de evacuación para encontrar la ruta más eficiente y rápida hacia la salida. Con ello se obtienen la identificación de las zonas más peligrosas del espacio y los tiempos de intervención.

***

#### RESULTADOS DE LAS PRUEBAS

###### 5.1 SÓTANO [REAL](https://github.com/Noelia-vera/TFG-Noelia-Fernandez-Talavera/blob/main/Resultados/primera%20prueba%20sotano.png) VS. [SIMULADO](https://github.com/Noelia-vera/TFG-Noelia-Fernandez-Talavera/blob/main/Resultados/sotano%20recorrido.png) 

En este apartado se compara el recorrido real y simulado que hizo el autómata en la primera prueba del CUS. en Youtube se encuentran los videos en primera y tercera persona de este recorrido.

* [VIDEO REAL  SÓTANO](https://www.youtube.com/watch?v=li0AAESpnBk&list=PL6ZMLEK_eBr83WLtaCB6bIBidZlwUOiJK&index=5)
