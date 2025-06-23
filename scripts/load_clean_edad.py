import pandas as pd
from pathlib import Path

def load_raw_data(filepath: Path) -> pd.DataFrame:
    """Carga el archivo CSV de datos crudos."""
    return pd.read_csv(filepath, sep=";", encoding="utf-8")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia y transforma el DataFrame de desocupados por tramo de edad."""
    df = df.rename(columns={
        "FREQ": "frecuencia",
        "INDICADOR": "indicador",
        "AREA_REF": "region",
        "EDAD": "tramo_edad",
        "TIME_PERIOD": "periodo",
        "OBS_VALUE": "valor",
        "OBS_STATUS": "estado",
    })
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    df = df[df["estado"] == "X"]
    cols_utiles = ["indicador", "periodo", "valor", "tramo_edad", "region", "frecuencia"]
    df = df[cols_utiles]
    df = df.dropna()
    df["periodo"] = df["periodo"].astype(str)
    return df

if __name__ == "__main__":
    # Rutas de archivos
    ruta_raw = "data/raw/poblacion_desocupada_tramo_edad.csv"
    ruta_clean = "data/processed/poblacion_desocupada_tramo_edad_limpio.csv"

    # Carga y limpieza
    df_raw = load_raw_data(ruta_raw)
    df_clean = clean_data(df_raw)

    # Guardar archivo limpio
    df_clean.to_csv(ruta_clean, index=False, encoding="utf-8")
    print("Archivo limpio guardado en:", ruta_clean)