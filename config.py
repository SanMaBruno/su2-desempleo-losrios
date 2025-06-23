from pathlib import Path

# Base directory del proyecto
BASE_DIR = Path(__file__).resolve().parent

# Rutas a las carpetas de datos
DATA_RAW = BASE_DIR / "data" / "raw"
DATA_PROCESSED = BASE_DIR / "data" / "processed"

# Archivos procesados específicos
FILE_TRAMO_EDAD = DATA_PROCESSED / "poblacion_desocupada_tramo_edad_limpio.csv"
FILE_SEXO = DATA_PROCESSED / "poblacion_desocupada_sexo_limpio.csv"
FILE_COMBINADO = DATA_PROCESSED / "poblacion_desocupada_combinado.csv"
FILE_TASA_SU2 = DATA_PROCESSED / "tasa_su2_desempleo_limpio.csv"