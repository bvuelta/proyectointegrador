# Importamos los módulos personalizados encargados de analizar procesos, memoria,
# auditar permisos del sistema de archivos y generar el informe final
from modules import procesos, memoria, auditoria, reporte


# Función principal que coordina todo el análisis del sistema
def main():

    # Obtenemos la lista de procesos en ejecución utilizando el módulo procesos
    procs = procesos.listar_procesos()

    # Obtenemos y procesamos la información de la memoria del sistema
    mem = memoria.parse_meminfo()

    # Definimos las rutas que se van a auditar, incluyendo directorios críticos
    # del sistema y el directorio personal del usuario
    rutas = ['/etc', '/var/log', '/usr/local/bin', '~']  # Mínimo 2 pedidas

    # Lista donde se almacenarán todas las rutas encontradas durante la auditoría
    all_paths = []

    # Recorremos cada una de las rutas definidas y añadimos todos los archivos
    # y directorios encontrados a la lista general
    for r in rutas:
        all_paths.extend(list(auditoria.recorrer_ruta(r)))

    # Analizamos los permisos de todas las rutas recopiladas para detectar
    # configuraciones peligrosas como permisos 777, SUID, SGID o escritura global
    audit_res = auditoria.permisos_riesgo(all_paths)

    # Generamos un informe en formato Markdown con los resultados del análisis
    # de procesos, memoria y auditoría de permisos
    reporte.generar_markdown(procs, mem, audit_res, output_path='informe.md')


# Punto de entrada del programa que asegura que la función main solo se ejecute
# cuando el archivo se lanza directamente y no cuando se importa como módulo
if __name__ == '__main__':
    main()

