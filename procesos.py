# modules/procesos.py
import psutil
from typing import List, Dict

def listar_procesos():
    procesos = []
    for p in psutil.process_iter(['pid','name','status','cpu_percent','memory_info','num_threads','exe']):
        try:
            info = p.info
            procesos.append({
                'pid': info['pid'],
                'name': info.get('name'),
                'status': info.get('status'),
                'cpu': info.get('cpu_percent'),        # necesita haber llamado cpu_percent anteriormente para ser preciso o usar interval en otra llamada
                'memory_mb': info.get('memory_info').rss / (1024*1024) if info.get('memory_info') else None,
                'threads': info.get('num_threads'),
                'exe': info.get('exe')
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return procesos

def top_n(procesos, key, n=10):
    return sorted(procesos, key=lambda x: x.get(key) or 0, reverse=True)[:n]
