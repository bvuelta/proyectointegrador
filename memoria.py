# Función que analiza la información de la memoria del sistema leyendo el archivo
# /proc/meminfo y convirtiendo los valores más relevantes de kB a MB
def parse_meminfo():
    mem = {}  # Diccionario donde se almacenarán los valores de memoria leídos del sistema

    # Abrimos el archivo /proc/meminfo en modo lectura para obtener información de la memoria
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            # Separamos cada línea en clave y valor usando el carácter ':'
            key, val = line.split(':', 1)

            # Limpiamos el valor, nos quedamos con el número y lo interpretamos como kB
            val = val.strip().split()[0]
            mem[key] = int(val)  # Guardamos el valor numérico en el diccionario

    # Función lambda que convierte el valor de una clave concreta de kB a MB
    to_mb = lambda k: mem.get(k, 0) / 1024.0

    # Devolvemos un diccionario con los principales datos de memoria expresados en MB
    return {
        'MemTotal_MB': to_mb('MemTotal'),
        'MemFree_MB': to_mb('MemFree'),
        'MemAvailable_MB': to_mb('MemAvailable'),
        'Cached_MB': to_mb('Cached'),
        'SwapTotal_MB': to_mb('SwapTotal'),
        'SwapFree_MB': to_mb('SwapFree')
    }

