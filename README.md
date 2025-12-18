Proyecto Integrador - Monitorización y Auditoría del Sistema Operativo

Asier Landaburu, Beñat Vuelta, Gaizka Hidalgo.

Este proyecto consiste en el desarrollo de una herramienta en **Python** que realiza tareas de **monitorización y auditoría de un sistema Linux**. El programa analiza procesos en ejecución, el estado de la memoria y los permisos del sistema de archivos, obteniendo la información directamente del sistema operativo mediante el uso a de archivos /proc.

El objetivo principal es comprender cómo el sistema operativo gestiona los recursos y la seguridad, así como automatizar la generación de un **informe técnico** con los resultados obtenidos.

Este trabajo se ha desarrollado como parte del **Proyecto Integrador de la asignatura Fundamentos de Computadores – Sistemas Operativos**.

---

# Objetivos

* Comprender la gestión de procesos e hilos en Linux.
* Analizar el uso real de memoria del sistema.
* Detectar configuraciones inseguras en permisos de archivos.
* Trabajar con información real del sistema operativo.
* Generar un informe automático en formato Markdown.

---

# Estructura del proyecto

```text
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

---

# Funcionalidad de los módulos

# Módulo de procesos (procesos.py)

* Lista los procesos en ejecución a partir de /proc.
* Muestra información básica como:

  * PID
  * Nombre del proceso
* (Opcionalmente ampliable a memoria o estado del proceso).

---

# Módulo de memoria (memoria.py)

* Analiza el archivo /proc/meminfo.
* Calcula y muestra:

  * Memoria total
  * Memoria libre
  * Memoria disponible
  * Caché
  * Swap
* Los valores se expresan en **MB**.

---

# Módulo de auditoría (auditoria.py)

* Recorre rutas críticas del sistema:

  * /etc
  * /var/log
  * /usr/local/bin
  * Directorio personal del usuario
* Detecta:

  * Archivos y directorios con permisos 777 o world-writable
  * Archivos con permisos SUID y SGID
  * Archivos modificados en las últimas 24 horas

---

# Módulo de reporte (reporte.py)

* Genera automáticamente un informe en formato **Markdown**.
* Incluye:

  * Resumen del estado del sistema
  * Resultados de la auditoría
  * Interpretación de los datos
  * Conclusiones y recomendaciones

---

# Ejecución del programa

- Requisitos

* Sistema operativo **Linux (Ubuntu)**
* Python **3.10 o superior**
* No requiere librerías externas (no se usa `psutil`)

# Ejecución

Desde el directorio raíz del proyecto:

bash
python3 main.py


El informe se generará automáticamente en la carpeta informes/.

---

# Informe generado

El programa crea un archivo informe.md que contiene:

* Estado general del sistema
* Listado de procesos
* Análisis de memoria
* Archivos y permisos de riesgo detectados
* Conclusiones y recomendaciones

Este informe puede convertirse fácilmente a PDF o HTML si se desea.

---

# Conclusiones

Este proyecto permite comprender de forma práctica el funcionamiento interno de un sistema Linux, especialmente en lo relativo a la gestión de procesos, memoria y seguridad del sistema de archivos. El uso de /proc garantiza independencia de librerías externas y un contacto directo con el sistema operativo.

---

