import pandas as pd
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from config import DATA_PROCESSED

file_path = os.path.join(DATA_PROCESSED, "poblacion_desocupada_combinado.csv")
df = pd.read_csv(file_path)

print(f"✅ Validando archivo: {file_path}")
print("📊 Columnas disponibles:", df.columns.tolist())
print("🔎 Nulos por columna:\n", df.isnull().sum())
print("📎 Registros duplicados:", df.duplicated().sum())
print("📏 Tamaño total:", df.shape)