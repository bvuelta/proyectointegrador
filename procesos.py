# Importar el módulo os
import os
# Función para listar los procesos de ejecución
def listar_procesos():
    procesos = []
    
    for pid in os.listdir('/proc'):
        if pid.isdigit(): # Verificar si es número
            try:
                with open(f'/proc/{pid}/status') as f: # Abrir el archivo (/proc/{pid}/status)
                    nombre = ""
                    for linea in f: # Leer linea a linea
                        if linea.startswith("Name:"):
                            nombre = linea.split()[1] # Si la línea comienza con "Name:" extraemos el nombre del proceso
                            break

                procesos.append({
                    'pid': int(pid), # Convertir PID a num. entero
                    'name': nombre # Nombre del proceso
                })

            except (FileNotFoundError, PermissionError): # Exception de error
                continue

    return procesos
