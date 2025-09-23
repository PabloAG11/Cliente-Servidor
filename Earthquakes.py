"""import urllib.request
import json
from datetime import datetime, timedelta, UTC

# Fechas (últimas 24h)
end = datetime.now(UTC)
start = end - timedelta(days=1)

url = (
    "https://earthquake.usgs.gov/fdsnws/event/1/query?"
    f"format=geojson&starttime={start.strftime('%Y-%m-%dT%H:%M:%S')}"
    f"&endtime={end.strftime('%Y-%m-%dT%H:%M:%S')}&minmagnitude=4.5&limit=10"
)

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

print("Eventos encontrados:", data["metadata"]["count"])
print("-" * 60)

for feat in data["features"]:
    props = feat["properties"]
    mag = props["mag"]
    place = props["place"]
    time_ms = props["time"]
    when = datetime.fromtimestamp(time_ms / 1000, tz=UTC).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"M{mag} - {place} - {when}")
"""
import urllib.request
import json
from datetime import datetime, timedelta, UTC
from collections import Counter

# Fechas (últimas 24h)
end = datetime.now(UTC)
start = end - timedelta(days=1)

url = (
    "https://earthquake.usgs.gov/fdsnws/event/1/query?"
    f"format=geojson&starttime={start.strftime('%Y-%m-%dT%H:%M:%S')}"
    f"&endtime={end.strftime('%Y-%m-%dT%H:%M:%S')}&minmagnitude=4.5&limit=50"
)

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

print("Eventos encontrados:", data["metadata"]["count"])
print("-" * 60)

# Contadores
lugares = []
magnitudes = []

for feat in data["features"]:
    props = feat["properties"]
    mag = props["mag"]
    place = props["place"]
    time_ms = props["time"]
    when = datetime.fromtimestamp(time_ms / 1000, tz=UTC).strftime("%Y-%m-%d %H:%M:%S UTC")

    print(f"M{mag:.1f} - {place} - {when}")

    magnitudes.append(mag)
    # Extraer país/región (última palabra del "place")
    if "," in place:
        region = place.split(",")[-1].strip()
    else:
        region = place.split(" ")[-1].strip()
    lugares.append(region)

print("\n📊 ESTADÍSTICAS")
print("-" * 60)

# Total
print(f"Total de terremotos: {len(magnitudes)}")

# Promedio de magnitudes
if magnitudes:
    promedio = sum(magnitudes) / len(magnitudes)
    print(f"Magnitud promedio: {promedio:.2f}")

# Por región
conteo_regiones = Counter(lugares)
print("\nTerremotos por región/país:")
for region, cantidad in conteo_regiones.most_common():
    print(f"  {region}: {cantidad}")
