# modules/reporte.py
import datetime

def generar_markdown(procs, mem, audit, output_path='informe.md'):
    now = datetime.datetime.now().isoformat()
    with open(output_path,'w') as f:
        f.write(f"# Informe de auditoría y monitorización\n\n")
        f.write(f"**Fecha:** {now}\n\n")
        # Memoria
        f.write("## Memoria\n")
        for k,v in mem.items():
            f.write(f"- {k}: {v:.2f} MB\n")
        f.write("\n## Procesos (resumen)\n")
        f.write(f"- Procesos detectados: {len(procs)}\n\n")
        f.write("### Top memoria (10)\n")
        for p in sorted(procs, key=lambda x: x.get('memory_mb') or 0, reverse=True)[:10]:
            f.write(f"- PID {p['pid']} {p['name']} {p.get('memory_mb'):.2f} MB\n")
        # Auditoría
        f.write("\n## Auditoría de permisos\n")
        for tipo in ['world_writable','permiso_777','suid','sgid','recientes']:
            f.write(f"### {tipo}\n")
            items = audit.get(tipo, [])
            if items:
                for it in items:
                    f.write(f"- {it}\n")
            else:
                f.write("- None\n")
        # Recomendaciones (puedes preparar plantillas)
        f.write("\n## Recomendaciones\n")
        f.write("- Cambiar permisos world-writable: chmod o chown según convenga.\n")
    return output_path
