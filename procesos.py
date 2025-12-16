# modules/procesos.py
import os

def listar_procesos():
    procesos = []
    
    for pid in os.listdir('/proc'):
        if pid.isdigit():
            try:
                with open(f'/proc/{pid}/status') as f:
                    nombre = ""
                    for linea in f:
                        if linea.startswith("Name:"):
                            nombre = linea.split()[1]
                            break

                procesos.append({
                    'pid': int(pid),
                    'name': nombre
                })

            except (FileNotFoundError, PermissionError):
                continue

    return procesos
