# Función que analiza la info. de memoria del sistema
def parse_meminfo():
    mem = {}
    with open('/proc/meminfo','r') as f:
        for line in f:
            key, val = line.split(':',1)
            val = val.strip().split()[0]  # Valor en kB
            mem[key] = int(val)
    # Convierte a MB
    to_mb = lambda k: mem.get(k,0) / 1024.0
    return {
        'MemTotal_MB': to_mb('MemTotal'),
        'MemFree_MB': to_mb('MemFree'),
        'MemAvailable_MB': to_mb('MemAvailable'),
        'Cached_MB': to_mb('Cached'),
        'SwapTotal_MB': to_mb('SwapTotal'),
        'SwapFree_MB': to_mb('SwapFree')
    }
