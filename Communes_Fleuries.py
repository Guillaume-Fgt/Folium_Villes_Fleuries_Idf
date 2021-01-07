import folium
import pandas as pd

communes_geo = "communes-ile-de-france - Copy2.geojson"
communes_fleuries = (
    "communes-dile-de-france-labellisees-villes-et-villages-fleuris-2020.csv"
)
communes_data = pd.read_csv(communes_fleuries)

m = folium.Map(
    location=[48.8, 2.3],
    width=750,
    height=500,
    zoom_start=8,
    tiles="CartoDB positron",
)

folium.Choropleth(
    geo_data=communes_geo,
    data=communes_data,
    name="Communes Fleuries",
    bins=4,
    fill_opacity=0.6,
    line_opacity=0.2,
    legend_name="Nombre de fleurs de la commune",
    columns=[
        "nom",
        "fleurs",
    ],
    key_on="feature.properties.nom",
    fill_color="YlGn",
).add_to(m)

# interactivity
style_function = lambda x: {
    "fillColor": "#ffffff",
    "color": "#000000",
    "fillOpacity": 0.1,
    "weight": 0.1,
}
highlight_function = lambda x: {
    "fillColor": "#000000",
    "color": "#000000",
    "fillOpacity": 0.50,
    "weight": 0.1,
}
NIL = folium.features.GeoJson(
    communes_geo,
    style_function=style_function,
    control=False,
    highlight_function=highlight_function,
    tooltip=folium.features.GeoJsonTooltip(
        fields=["nom", "code", "fleurs"],
        aliases=["Commune: ", "Code Postal: ", "Nbr Fleurs: "],
        style=(
            "background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"
        ),
    ),
)
m.add_child(NIL)
m.keep_in_front(NIL)
#

folium.LayerControl().add_to(m)
m.save("map.html")