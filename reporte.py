# Importamos el módulo datetime para obtener la fecha y hora actual en la que se genera el informe
import datetime


# Función que genera un informe en formato Markdown con la información de memoria,
# procesos y auditoría de permisos, guardándolo en el archivo especificado
def generar_markdown(procs, mem, audit, output_path='informe.md'):
    # Obtenemos la fecha y hora actual en formato ISO
    now = datetime.datetime.now().isoformat()

    # Abrimos el archivo de salida en modo escritura para generar el informe
    with open(output_path, 'w') as f:
        # Escribimos el título principal del informe y la fecha
        f.write(f"# Informe de auditoría y monitorización\n\n")
        f.write(f"**Fecha:** {now}\n\n")

        # Sección de memoria: listamos los valores de memoria obtenidos del sistema
        f.write("## Memoria\n")
        for k, v in mem.items():
            f.write(f"- {k}: {v:.2f} MB\n")

        # Sección de procesos: resumen del total de procesos detectados
        f.write("\n## Procesos (resumen)\n")
        f.write(f"- Procesos detectados: {len(procs)}\n\n")

        # Mostramos los 10 procesos que más memoria consumen, ordenados de mayor a menor
        f.write("### Top memoria (10)\n")
        for p in sorted(procs, key=lambda x: x.get('memory_mb') or 0, reverse=True)[:10]:
            f.write(f"- PID {p['pid']} {p['name']}\n")

        # Sección de auditoría de permisos: listamos los archivos y directorios según tipo de riesgo
        f.write("\n## Auditoría de permisos\n")
        for tipo in ['world_writable', 'permiso_777', 'suid', 'sgid', 'recientes']:
            f.write(f"### {tipo}\n")
            items = audit.get(tipo, [])
            # Si hay elementos de riesgo, los listamos; si no, indicamos "None"
            if items:
                for it in items:
                    f.write(f"- {it}\n")
            else:
                f.write("- None\n")

        # Sección de recomendaciones básicas basadas en la auditoría realizada
        f.write("\n## Recomendaciones\n")
        f.write("- Cambiar permisos world-writable: chmod o chown según convenga.\n")

    # Devolvemos la ruta del archivo generado
    return output_path

