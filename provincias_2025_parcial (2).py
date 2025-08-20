import requests
import pandas as pd

# Coordenadas de las capitales provinciales
provincias_coords = {
    "Buenos Aires": (-34.61315, -58.37723),
    "Catamarca": (-28.46957, -65.78524),
    "Chaco": (-27.45139, -58.98667),
    "Chubut": (-43.30016, -65.10228),
    "Córdoba": (-31.4135, -64.18105),
    "Corrientes": (-27.4806, -58.8341),
    "Entre Ríos": (-31.73333, -60.53333),
    "Formosa": (-26.18489, -58.17313),
    "Jujuy": (-24.18394, -65.33122),
    "La Pampa": (-36.61667, -64.28333),
    "La Rioja": (-29.41308, -66.8558),
    "Mendoza": (-32.8908, -68.8272),
    "Misiones": (-27.36679, -55.89608),
    "Neuquén": (-38.95161, -68.0591),
    "Río Negro": (-40.81345, -62.99668),
    "Salta": (-24.7859, -65.41166),
    "San Juan": (-31.5375, -68.53639),
    "San Luis": (-33.29501, -66.33563),
    "Santa Cruz": (-51.63333, -69.21667),
    "Santa Fe": (-31.63333, -60.7),
    "Santiago del Estero": (-27.79511, -64.26149),
    "Tierra del Fuego": (-54.80191, -68.30295),
    "Tucumán": (-26.82414, -65.2226)
}

# Lista para acumular datos
datos_totales = []

print("⏳ Descargando datos 2025 (01/01 al 11/08) de todas las provincias argentinas...")

for provincia, (lat, lon) in provincias_coords.items():
    print(f"📍 {provincia}...")
    
    url = (
        "https://archive-api.open-meteo.com/v1/archive"
        f"?latitude={lat}&longitude={lon}"
        "&start_date=2025-01-01&end_date=2025-08-11"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&timezone=America/Argentina/Buenos_Aires"
    )
    
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    df = pd.DataFrame({
        "Provincia": provincia,
        "Fecha": data["daily"]["time"],
        "Temperatura Máxima (°C)": data["daily"]["temperature_2m_max"],
        "Temperatura Mínima (°C)": data["daily"]["temperature_2m_min"]
    })
    
    datos_totales.append(df)

# Unir todos los DataFrames
df_total = pd.concat(datos_totales, ignore_index=True)

# Guardar CSV
df_total.to_csv("temperaturas_argentina_2025_enero_a_agosto.csv", index=False, encoding="utf-8")

print("✅ CSV generado: temperaturas_argentina_2025_enero_a_agosto.csv")
