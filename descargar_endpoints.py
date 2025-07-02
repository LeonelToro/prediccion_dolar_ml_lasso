import os
import requests
import pandas as pd

# CONFIGURACIÓN
TOKEN = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODI2NzAyOTcsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJsZW9uZWwudG9ybzkzQGdtYWlsLmNvbSJ9.Q3BQQG0KxCw_PPRh2qraZpdI0KDAlLzm12OfQdPX5s_O7zB4E1GYOKIeMjICtS8cRJm6mK2hkjJULrnbBR2T4w"
OUTPUT_DIR = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\BCRA\data\raw"
BASE_URL = "https://api.estadisticasbcra.com/"
HEADERS = {"Authorization": f"BEARER {TOKEN}"}

# Definir los endpoints de la API del BCRA
ENDPOINTS = {
    "usd_oficial": "usd_of",                         # Dólar oficial mayorista
    "usd_minorista": "usd_of_minorista",             # Dólar oficial minorista (consumo)
    "usd_general": "usd",                            # Promedio de distintos tipos de dólar
    "brecha_usd": "var_usd_vs_usd_of",              # Brecha entre el dólar oficial y el dólar general
    "inflacion": "inflacion_mensual_oficial",       # Inflación mensual oficial
    "leliq": "leliq",                                # Tasa LELIQ
    "tasa_pase_pasivas_1_dia": "tasa_pase_pasivas_1_dia",         # Tasa pase pasiva
    "tasa_depositos_30_dias": "tasa_depositos_30_dias", # Tasa de depósitos a 30 días
    "reservas": "reservas",                          # Reservas internacionales brutas
    "base_monetaria": "base",                        # Base monetaria (M2)
    "cer": "cer",                                    # Coeficiente CER
    "uva": "uva"                                     # Unidad de Valor Adquisitivo
}

# Función para descargar y guardar los datos de un endpoint específico
def download_and_save(endpoint_name, endpoint_url):
    print(f"Descargando {endpoint_name}...")
    url = BASE_URL + endpoint_url
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        output_path = os.path.join(OUTPUT_DIR, f"{endpoint_name}.csv")
        df.to_csv(output_path, index=False)
        print(f"{endpoint_name} guardado en {output_path}")
        return True
    else:
        print(f"Error al descargar {endpoint_name}: {response.status_code}")
        return False

# Función principal para descargar todos los endpoints y guardarlos en archivos CSV
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    success_count = 0

    for name, endpoint in ENDPOINTS.items():
        if download_and_save(name, endpoint):
            success_count += 1

    print(f"\n{success_count} archivos descargados satisfactoriamente.")

if __name__ == "__main__":
    main()