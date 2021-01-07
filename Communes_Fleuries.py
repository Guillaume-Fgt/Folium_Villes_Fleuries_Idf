import folium


communes_geo = "communes-ile-de-france - Copy2.geojson"


m = folium.Map(
    location=[48.7, 2.3],
    zoom_start=9,
    zoom_control=False,
    tiles=None,
)

folium.TileLayer("CartoDB positron", name="Light Map", control=False).add_to(m)

colormap = ["#edf8e9", "#bae4b3", "#74c476", "#31a354", "#006d2c"]

# interactivity
style_function = lambda x: {
    "fillColor": colormap[x["properties"]["fleurs"]],
    "color": "#000000",
    "fillOpacity": 0.5,
    "weight": 0.1,
}
highlight_function = lambda x: {
    "fillColor": "#000000",
    "color": "#000000",
    "fillOpacity": 0.50,
    "weight": 0.3,
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
        sticky=False,
    ),
)
m.add_child(NIL)
m.keep_in_front(NIL)
#

folium.LayerControl().add_to(m)
m.save("map.html")