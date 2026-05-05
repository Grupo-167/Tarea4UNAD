import logging
import os
from datetime import datetime

LOG_FILE = "sistema_fj.log"

# Crear el logger nombrado
logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.DEBUG)

# Handler para archivo — guarda todo desde DEBUG
file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Handler para consola — solo muestra WARNING en adelante
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# Formato compartido
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Agregar handlers directamente al logger nombrado
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Evitar que los mensajes suban al logger raíz
logger.propagate = False

# ─── Funciones de acceso rápido ───

def log_evento(mensaje: str):
# Registra un evento informativo general en el sistema.
    logger.info(mensaje)

def log_advertencia(mensaje: str):
# Registra una advertencia que no detiene el sistema pero indica un posible problema.
    logger.warning(mensaje)

def log_error(mensaje: str, excepcion: Exception = None):
# Registra un error. Si se proporciona la excepción, incluye su tipo y mensaje.
    if excepcion:
        logger.error(f"{mensaje} | Excepción: {type(excepcion).__name__}: {excepcion}")
    else:
        logger.error(mensaje)

def log_critico(mensaje: str, excepcion: Exception = None):
# Registra un error crítico. Si se proporciona la excepción, incluye su traceback.
    if excepcion:
        logger.critical(f"{mensaje} | Excepción: {type(excepcion).__name__}: {excepcion}")
    else:
        logger.critical(mensaje)

def log_inicio_sesion():
# Registra el inicio de una nueva sesión del sistema, con un separador visual.
    separador = "=" * 60
    logger.info(separador)
    logger.info(f"NUEVA SESIÓN INICIADA - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(separador)

def log_cierre_sesion():
# Registra el cierre de la sesión actual del sistema.
    logger.info("SESIÓN CERRADA CORRECTAMENTE")
    logger.info("=" * 60)