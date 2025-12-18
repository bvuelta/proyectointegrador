# Importar librerías os, stat, time y path
import os  # Módulo estándar para operaciones del sistema operativo (rutas, recorridos, permisos básicos).
import stat  # Proporciona constantes y utilidades para interpretar bits de permisos en st_mode.
import time  # Permite trabajar con tiempos Unix (epoch) y obtener el tiempo actual.
from pathlib import Path  # Clase Path para manejar rutas de forma orientada a objetos y portable.


# Función para recorrer una ruta del sistema de archivos
def recorrer_ruta(root_path, max_depth=5):  # Recibe una ruta raíz y un parámetro de profundidad (no usado)
    root_path = Path(root_path).expanduser()  # Convierte la ruta en objeto Path y expande '~' al home del usuario

    # os.walk recorre el árbol de directorios a partir de root_path
    # Devuelve en cada iteración: ruta actual, lista de subdirectorios y lista de archivos
    for dirpath, dirnames, filenames in os.walk(root_path):

  
        for name in filenames + dirnames:
            try:
                # Construimos la ruta completa uniendo el directorio actual con el nombre
                full = Path(dirpath) / name

                # Devolvemos la ruta como generador para procesarla una a una
                yield full

            except Exception:
                # Si ocurre cualquier error (permisos, rutas inválidas, etc.),
                # se ignora y se continúa con el siguiente archivo/directorio
                continue


# Función que analiza permisos potencialmente peligrosos
def permisos_riesgo(paths):
    world_writable = []  # Archivos/directorios escribibles por cualquier usuario
    permiso_777 = []     # Archivos/directorios con permisos 777
    suid = []            # Archivos con el bit SUID activado
    sgid = []            # Archivos/directorios con el bit SGID activado
    recientes = []       # Archivos modificados en las últimas 24 horas

    ahora = time.time()  # Tiempo actual en segundos desde el epoch Unix

    # Recorremos todas las rutas recibidas
    for p in paths:
        try:
            st = p.stat()  # Obtenemos la información del archivo (permisos, fechas, etc.)
        except Exception:
            # Si no se puede acceder a los metadatos, se ignora la ruta
            continue

        mode = st.st_mode  # Guardamos el modo del archivo 

        # Comprobación de permisos world writable (escritura para otros)
        if bool(mode & stat.S_IWOTH):
            world_writable.append(str(p))

        # Comprobación de permisos exactamente 777
        if stat.S_IMODE(mode) == 0o777:
            permiso_777.append(str(p))

        # Comprobación del bit SUID 
        if bool(mode & stat.S_ISUID):
            suid.append(str(p))

        # Comprobación del bit SGID 
        if bool(mode & stat.S_ISGID):
            sgid.append(str(p))

        # Comprobación de archivos modificados en las últimas 24 horas
        if (ahora - st.st_mtime) < 24 * 3600:
            recientes.append(str(p))

    # Devolvemos un diccionario con todas las categorías de riesgo detectadas
    return {
        'world_writable': world_writable,
        'permiso_777': permiso_777,
        'suid': suid,
        'sgid': sgid,
        'recientes': recientes
    }

