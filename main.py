# main.py
from modules import procesos, memoria, auditoria, reporte

def main():
    # Procesos
    procs = procesos.listar_procesos()
    # Memoria
    mem = memoria.parse_meminfo()
    # Auditoría: recorrer rutas
    rutas = ['/etc','/var/log','/usr/local/bin', '~']  # mínimo 2 pedidas
    all_paths = []
    for r in rutas:
        all_paths.extend(list(auditoria.recorrer_ruta(r)))
    audit_res = auditoria.permisos_riesgo(all_paths)
    # Generar reporte
    reporte.generar_markdown(procs, mem, audit_res, output_path='informe.md')

if __name__ == '__main__':
    main()
