import folium
import pandas as pd

villes_fleuries_json = (
    "communes-dile-de-france-labellisees-villes-et-villages-fleuris-2020.json"
)
villes_json = "communes-ile-de-france.geojson"

m = folium.Map(
    location=[48.8601, 2.3557],
    width=750,
    height=500,
    zoom_start=8,
    tiles="CartoDB positron",
)

highlight_function = lambda x: {
    "fillColor": "#000000",
    "color": "#000000",
    "fillOpacity": 0.50,
    "weight": 0.1,
}

folium.GeoJson(
    villes_json,
    tooltip=folium.features.GeoJsonTooltip(fields=["nom"]),
    highlight_function=highlight_function,
).add_to(m)


m.save("map2.html")