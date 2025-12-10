# modules/auditoria.py
import os
import stat
import time
from pathlib import Path

def recorrer_ruta(root_path, max_depth=5):
    root_path = Path(root_path).expanduser()
    for dirpath, dirnames, filenames in os.walk(root_path):
        for name in filenames + dirnames:
            try:
                full = Path(dirpath) / name
                yield full
            except Exception:
                continue

def permisos_riesgo(paths):
    world_writable = []
    permiso_777 = []
    suid = []
    sgid = []
    recientes = []
    ahora = time.time()
    for p in paths:
        try:
            st = p.stat()
        except Exception:
            continue
        mode = st.st_mode
        # world writable?
        if bool(mode & stat.S_IWOTH):
            world_writable.append(str(p))
        # 777?
        if stat.S_IMODE(mode) == 0o777:
            permiso_777.append(str(p))
        # SUID
        if bool(mode & stat.S_ISUID):
            suid.append(str(p))
        # SGID
        if bool(mode & stat.S_ISGID):
            sgid.append(str(p))
        # modificados en las últimas 24h
        if (ahora - st.st_mtime) < 24*3600:
            recientes.append(str(p))
    return {
        'world_writable': world_writable,
        'permiso_777': permiso_777,
        'suid': suid,
        'sgid': sgid,
        'recientes': recientes
    }
