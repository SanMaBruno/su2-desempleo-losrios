import pandas as pd
from pathlib import Path

def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo en {path}")
    return pd.read_csv(path, delimiter=';', encoding='utf-8')

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns={
        'DATAFLOW': 'dataflow',
        'FREQ': 'frecuencia',
        'INDICADOR': 'indicador',
        'SEXO': 'sexo',
        'AREA_REF': 'region',
        'TIME_PERIOD': 'periodo',
        'OBS_VALUE': 'valor',
        'FUENTE': 'fuente'
    })

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = rename_columns(df)
    df = df[['indicador', 'sexo', 'region', 'periodo', 'valor']]
    df = df[df['region'] == '14']  # Región de Los Ríos
    df = df.dropna(subset=['valor'])
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
    df['periodo'] = df['periodo'].astype(str)
    df['sexo'] = df['sexo'].astype(str)
    return df.dropna()

def save_output(df: pd.DataFrame, output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Archivo guardado en: {output_path}")

def main():
    input_file = Path("data/raw/poblacion_desocupada_sexo.csv")
    output_file = Path("data/processed/poblacion_desocupada_sexo_limpio.csv")

    try:
        df_raw = load_csv(input_file)
        print("📥 Datos cargados correctamente.")
        df_clean = clean_data(df_raw)
        save_output(df_clean, output_file)
    except Exception as e:
        print(f"❌ Error en el procesamiento: {e}")

if __name__ == "__main__":
    main()