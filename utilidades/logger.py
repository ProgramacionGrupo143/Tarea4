from datetime import datetime
from pathlib import Path

RUTA_LOG :Path = Path("logs/eventos.log")

def registrar_evento(mensaje:str)->None:
    RUTA_LOG.parent.mkdir(exist_ok=True)

    with open(RUTA_LOG,"a",encoding="utf-8") as archivo:
        archivo.write(f"[EVENTO] {datetime.now()} - {mensaje}\n")

def registrar_error(mensaje:str)->None:
    RUTA_LOG.parent.mkdir(exist_ok=True)

    with open(RUTA_LOG,"a",encoding="utf-8") as archivo:
        archivo.write(f"[ERROR] {datetime.now()} - {mensaje}\n")