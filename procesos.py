# Importamos el módulo os para interactuar con el sistema de archivos y acceder
# a la información de los procesos a través del directorio /proc
import os


# Función que lista los procesos en ejecución leyendo la información disponible
# en el sistema de archivos virtual /proc
def listar_procesos():
    procesos = []  # Lista donde se almacenarán los procesos encontrados

    # Recorremos todas las entradas del directorio /proc
    for pid in os.listdir('/proc'):

        # Comprobamos que el nombre del directorio sea numérico, lo que indica un PID
        if pid.isdigit():
            try:
                # Abrimos el archivo status del proceso para obtener información básica
                with open(f'/proc/{pid}/status') as f:
                    nombre = ""  # Variable donde se guardará el nombre del proceso

                    # Leemos el archivo línea a línea hasta encontrar el nombre
                    for linea in f:
                        if linea.startswith("Name:"):
                            # Extraemos el nombre del proceso cuando encontramos la línea adecuada
                            nombre = linea.split()[1]
                            break

                # Añadimos el proceso a la lista como un diccionario con su PID y nombre
                procesos.append({
                    'pid': int(pid),
                    'name': nombre
                })

            # Capturamos errores habituales como procesos que finalizan o falta de permisos
            except (FileNotFoundError, PermissionError):
                continue

    # Devolvemos la lista completa de procesos encontrados
    return procesos

