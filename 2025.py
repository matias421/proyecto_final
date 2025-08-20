import pandas as pd
import matplotlib.pyplot as plt

# Cargar CSV
df_temp = pd.read_csv("temperaturas_argentina_2025_enero_a_agosto.csv")
df_temp["Fecha"] = pd.to_datetime(df_temp["Fecha"])

# Mostrar información en la terminal 
print("\n--- Primeras 7 filas ---")
print(df_temp.head(7))
print("\n--- Últimas 3 filas ---")
print(df_temp.tail(3))
print("\n--- Columnas ---")
print(df_temp.columns)
print("\n--- Dimensiones del DataFrame ---")
print(df_temp.shape)
print("\n--- Estadísticas descriptivas ---")
print(df_temp.describe())

# Promedio temperatura máxima 
promedio_max = df_temp.groupby("Provincia")["Temperatura Máxima (°C)"].mean().sort_values(ascending=False)
print("\n--- Promedio de temperatura máxima por provincia ---")
print(promedio_max)

plt.figure(figsize=(8,6))
promedio_max.plot(kind="bar", color="red")
plt.title("Promedio Temperatura Máxima (ene-ago 2025)")
plt.ylabel("°C")
plt.xlabel("Provincia")
plt.xticks(rotation=75)
plt.tight_layout()
plt.savefig("promedio_max.png")
plt.show()

# Promedio temperatura mínima
promedio_min = df_temp.groupby("Provincia")["Temperatura Mínima (°C)"].mean().sort_values(ascending=False)
print("\n--- Promedio de temperatura mínima por provincia ---")
print(promedio_min)

plt.figure(figsize=(8,6))
promedio_min.plot(kind="bar", color="blue")
plt.title("Promedio Temperatura Mínima (ene-ago 2025)")
plt.ylabel("°C")
plt.xlabel("Provincia")
plt.xticks(rotation=75)
plt.tight_layout()
plt.savefig("promedio_min.png")
plt.show()

# Días extremos
def clasificar_dia(row):
    if row["Temperatura Máxima (°C)"] >= 35:
        return "Caluroso Extremo"
    elif row["Temperatura Mínima (°C)"] <= 0:
        return "Frío Extremo"
    else:
        return "Normal"

df_temp["Tipo Día"] = df_temp.apply(clasificar_dia, axis=1)
conteo = df_temp.groupby(["Provincia", "Tipo Día"]).size().unstack(fill_value=0)

print("\n--- Cantidad de días por tipo ---")
print(conteo)

plt.figure(figsize=(10,6))
conteo.plot(kind="bar", stacked=True, color=["red", "blue", "gray"])
plt.title("Cantidad de Días Extremos por Provincia (ene-ago 2025)")
plt.ylabel("Cantidad de días")
plt.xlabel("Provincia")
plt.xticks(rotation=75)
plt.legend(title="Tipo Día")
plt.tight_layout()
plt.savefig("dias_extremos.png")
plt.show()

# Análisis adicional
print("\nAnálisis:")
print("Provincia con más días calurosos extremos:", conteo["Caluroso Extremo"].idxmax())
print("Provincia con más días fríos extremos:", conteo["Frío Extremo"].idxmax())
print("Provincia con mayor promedio de temperatura máxima:", promedio_max.idxmax())
print("Provincia con mayor promedio de temperatura mínima:", promedio_min.idxmax())
