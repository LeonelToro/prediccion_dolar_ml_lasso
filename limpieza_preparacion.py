import os
import pandas as pd

# Rutas
base_path = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\BCRA\data\raw"
processed_path = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\BCRA\data\processed"
os.makedirs(processed_path, exist_ok=True)

# Archivo de salida
output_file = os.path.join(processed_path, "consolidado.csv")

# Detectar todos los archivos .csv
csv_files = [f for f in os.listdir(base_path) if f.endswith(".csv")]

# Armar diccionario automáticamente: {'nombre_sin_extension': 'archivo.csv'}
files = {os.path.splitext(f)[0]: f for f in csv_files}

# Mostrar para confirmar
print("Archivos detectados:")
for key, value in files.items():
    print(f"{key}: {value}")

dfs = {}

for key, filename in files.items():
    path = os.path.join(base_path, filename)
    df = pd.read_csv(path)
    # Convertir columna 'd' a datetime y renombrar columnas para merge
    df["d"] = pd.to_datetime(df["d"])
    df.rename(columns={"v": key}, inplace=True)
    dfs[key] = df

# Merges iterativos usando 'd' como clave con outer join
from functools import reduce

df_merged = reduce(
    lambda left, right: pd.merge(left, right, on="d", how="outer"),
    dfs.values()
)

# Filtrar por fecha mínima
fecha_minima = pd.Timestamp("2010-06-01")
df_merged = df_merged.loc[df_merged["d"] >= fecha_minima].copy()

# Ordenar por fecha
df_merged.sort_values("d", inplace=True)

# Reiniciar índice
df_merged.reset_index(drop=True, inplace=True)

print(f"Dimensiones del DataFrame consolidado: {df_merged.shape}")
print(f"Fechas: {df_merged['d'].min()} a {df_merged['d'].max()}")

# Setear 'd' como índice
df_merged.set_index("d", inplace=True)

# Calcular promedio por mes
df_mensual = df_merged.resample("M").mean()

# Resetear el índice para volver a tener la columna 'fecha'
df_mensual.reset_index(inplace=True)
df_mensual.rename(columns={"d": "fecha"}, inplace=True)

# Verificar las dimensiones y fechas del DataFrame mensual
print(f"Dimensiones mensuales: {df_mensual.shape}")
print(f"Fechas: {df_mensual['fecha'].min().date()} a {df_mensual['fecha'].max().date()}")

# Evaluar cuántos valores no nulos hay por fila (mes)
df_mensual["completitud"] = df_mensual.notna().sum(axis=1)

# Detectar el último mes con suficientes datos (ej: al menos 5 columnas con datos)
df_mensual = df_mensual[df_mensual["completitud"] >= 5].copy()

# Eliminar la columna auxiliar
df_mensual.drop(columns="completitud", inplace=True)

# Mostrar fechas finales
print(f"Última fecha con datos suficientes: {df_mensual['fecha'].max().date()}")

# Guardar el DataFrame consolidado
df_mensual.to_csv(output_file, index=False)

print(f"Archivo guardado exitosamente en: {output_file}")
print(f"Dimensiones finales: {df_mensual.shape}")
