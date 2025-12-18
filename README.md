Asier Landaburu, Beñat Vuelta, Gaizka Hidalgo.
# Proyecto Integrador - Monitorización y Auditoría del Sistema Operativo

Introducción:
---
Este proyecto consiste en el desarrollo de una herramienta en Python orientada a la monitorización y auditoría básica de un sistema operativo Linux. El programa obtiene información real del propio sistema para analizar cómo se gestionan los procesos en ejecución, el uso de la memoria y la configuración de permisos de archivos. A partir de estos datos, la aplicación genera automáticamente un informe técnico que resume el estado del sistema, identifica posibles riesgos y ofrece una interpretación de los resultados.

Estructura:
---
El proyecto está organizado en varios módulos independientes, cada uno encargado de una parte concreta del análisis. Esta organización modular permite que el código sea más claro, mantenible y fácil de ampliar. El programa cuenta con un archivo principal, denominado main.py, que actúa como punto de entrada y coordina el funcionamiento del resto de módulos encargados de la monitorización de procesos, el análisis de memoria, la auditoría de seguridad y la generación del informe final.

```
proyecto_monitorizacion_auditoria/
├── main.py
├── modules/
│   ├── procesos.py
│   ├── memoria.py
│   ├── auditoria.py
│   └── reporte.py
├── informes/
│   └── informe.md
└── README.md
```

Funcionamiento del programa y descripción de los módulos:
---
El archivo main.py es el encargado de iniciar la ejecución del programa. Desde este módulo se llaman de forma ordenada al resto de módulos del proyecto, recopilando la información obtenida por cada uno de ellos. Una vez recogidos todos los datos, main.py los envía al módulo responsable de generar el informe automático, de modo que el usuario solo necesita ejecutar un único archivo para obtener el análisis completo del sistema.

El módulo procesos.py se encarga de la monitorización de los procesos que se están ejecutando en el sistema en ese momento. Este módulo obtiene información relevante de cada proceso, como su identificador (PID), el nombre, el estado, el uso de CPU, el consumo de memoria, el número de hilos y, cuando es posible, la ruta del ejecutable asociado. Para ello, se accede a la información disponible en el sistema de archivos /proc o se utiliza la librería psutil si está disponible. Gracias a este análisis, es posible tener una visión clara de la carga de trabajo del sistema y detectar procesos que consumen una cantidad elevada de recursos.

El módulo memoria.py se centra en el análisis del estado de la memoria del sistema. Para ello, lee y procesa el contenido del archivo /proc/meminfo, a partir del cual calcula la memoria total, la memoria libre, la memoria disponible, la memoria utilizada como caché y el uso de memoria swap. Todos estos valores se convierten a megabytes para facilitar su comprensión. Este módulo permite entender cómo se está utilizando la memoria en el sistema y si existen posibles problemas de falta de recursos.

El módulo auditoria.py realiza una auditoría básica de seguridad sobre el sistema de archivos. Su función principal es recorrer varias rutas consideradas críticas, como /etc, /var/log, /usr/local/bin y el directorio personal del usuario, con el fin de detectar configuraciones potencialmente inseguras. Durante este proceso, el módulo identifica archivos y directorios con permisos de escritura para todos los usuarios, permisos 777, archivos con los bits SUID y SGID activados, así como archivos que han sido modificados en las últimas 24 horas. Esta información resulta útil para detectar posibles riesgos de seguridad o malas configuraciones.

Por último, el módulo informe.py se encarga de generar el informe automático del proyecto. A partir de los datos recopilados por los módulos anteriores, este archivo crea un informe en formato de texto o Markdown que incluye un resumen del estado de los procesos, el análisis de la memoria y los resultados de la auditoría de permisos. Además, el informe contiene una interpretación de los resultados obtenidos y una sección de conclusiones y recomendaciones, lo que permite presentar la información de forma clara y estructurada.

Requisitos y dependencias:
---
Para poder ejecutar correctamente el programa es necesario disponer de un sistema operativo Linux y tener instalada una versión de Python 3.8 o superior. El programa necesita permisos de lectura sobre el sistema de archivos /proc y sobre las rutas que se auditan. De forma opcional, puede utilizarse la librería psutil para facilitar la obtención de información sobre los procesos, la cual puede instalarse mediante el gestor de paquetes pip.

Instrucciones de ejecución:
---
Para ejecutar el programa, primero es necesario copiar o clonar el proyecto en un sistema Linux. Una vez situado en el directorio del proyecto, se debe ejecutar el archivo principal utilizando el intérprete de Python. Al finalizar la ejecución, el programa mostrará parte de la información por pantalla y generará automáticamente el archivo de informe en el directorio del proyecto, el cual contendrá todos los resultados del análisis realizado.
