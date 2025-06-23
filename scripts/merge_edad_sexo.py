import pandas as pd

# Cargar los datasets limpios
df_edad = pd.read_csv("data/processed/poblacion_desocupada_tramo_edad_limpio.csv")
df_sexo = pd.read_csv("data/processed/poblacion_desocupada_sexo_limpio.csv")

# Añadir columna 'dimension' y 'categoria' para facilitar análisis
df_edad["dimension"] = "tramo_edad"
df_edad["categoria"] = df_edad["tramo_edad"]

df_sexo["dimension"] = "sexo"
df_sexo["categoria"] = df_sexo["sexo"]

# Unificar columnas comunes
columnas_comunes = ["indicador", "periodo", "valor", "region", "dimension", "categoria"]
df_edad = df_edad[columnas_comunes]
df_sexo = df_sexo[columnas_comunes]

# Combinar ambos
df_combinado = pd.concat([df_edad, df_sexo], ignore_index=True)

# Guardar resultado
output_path = "data/processed/poblacion_desocupada_combinado.csv"
df_combinado.to_csv(output_path, index=False)

print(f"✅ Datos combinados guardados en: {output_path}")