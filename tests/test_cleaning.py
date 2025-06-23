import pandas as pd
from pathlib import Path
from scripts.load_clean_edad import load_raw_data, clean_data

def test_clean_data_structure():
    input_path = Path("data/raw/poblacion_desocupada_tramo_edad.csv")
    df_raw = load_raw_data(input_path)
    df_clean = clean_data(df_raw)

    # Verifica columnas esperadas
    expected_columns = ['indicador', 'periodo', 'valor', 'tramo_edad', 'region', 'frecuencia']
    assert list(df_clean.columns) == expected_columns

def test_clean_data_no_nulls():
    input_path = Path("data/raw/poblacion_desocupada_tramo_edad.csv")
    df_raw = load_raw_data(input_path)
    df_clean = clean_data(df_raw)

    # Verifica que no haya nulos en las columnas importantes
    assert df_clean['valor'].isnull().sum() == 0
    assert df_clean['periodo'].isnull().sum() == 0

def test_clean_data_value_types():
    input_path = Path("data/raw/poblacion_desocupada_tramo_edad.csv")
    df_raw = load_raw_data(input_path)
    df_clean = clean_data(df_raw)

    # Verifica tipos de datos
    assert pd.api.types.is_numeric_dtype(df_clean['valor'])
    assert pd.api.types.is_string_dtype(df_clean['periodo'])