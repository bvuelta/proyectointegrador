# proyectointegrador
# Proyecto de Monitorización y Auditoría del Sistema

## 📌 Descripción

Este proyecto consiste en el desarrollo de una herramienta en **Python** que realiza tareas de **monitorización y auditoría de un sistema Linux**. El programa analiza procesos en ejecución, el estado de la memoria y los permisos del sistema de archivos, obteniendo la información directamente del sistema operativo mediante el uso del pseudo–sistema de archivos `/proc`.

El objetivo principal es comprender cómo el sistema operativo gestiona los recursos y la seguridad, así como automatizar la generación de un **informe técnico** con los resultados obtenidos.

Este trabajo se ha desarrollado como parte del **Proyecto Integrador de la asignatura Fundamentos de Computadores – Sistemas Operativos**.

---

## 🎯 Objetivos

* Comprender la gestión de procesos e hilos en Linux.
* Analizar el uso real de memoria del sistema.
* Detectar configuraciones inseguras en permisos de archivos.
* Trabajar con información real del sistema operativo.
* Generar un informe automático en formato Markdown.

---

## 🗂️ Estructura del proyecto

```text
proyecto_monitorizacion_auditoria/
├── main.py
├── modules/
│   ├── procesos.py
│   ├── memoria.py
│   ├── audit
```
