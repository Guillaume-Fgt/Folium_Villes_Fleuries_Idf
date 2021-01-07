import folium
import branca


communes_geo = "communes-ile-de-france - Copy2.geojson"


m = folium.Map(
    location=[48.7, 2.3],
    zoom_start=9,
    tiles=None,
)

folium.TileLayer("CartoDB positron", name="Light Map", control=False).add_to(m)

colorlist = ["#f6eff7", "#bdc9e1", "#67a9cf", "#1c9099", "#016c59"]
colormap = branca.colormap.StepColormap(
    colorlist,
    index=[0, 1, 2, 3, 4],
    vmin=0,
    vmax=4,
    caption="Nbr de fleurs de la commune",
)

# interactivity
style_function = lambda x: {
    # "fillColor": colormap[x["properties"]["fleurs"]],
    "fillColor": colormap(
        x["properties"]["fleurs"] + 0.1
    ),  # +0.1 pour gérer l'index de colormap
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
    highlight_function=highlight_function,
    tooltip=folium.features.GeoJsonTooltip(
        fields=["nom", "code", "fleurs"],
        aliases=["Commune: ", "Code Postal: ", "Nbr Fleurs: "],
        style=(
            "background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"
        ),
        sticky=False,
    ),
    name="Communes fleuries 2020 IDF",
)
m.add_child(NIL)
m.keep_in_front(NIL)
#
colormap.add_to(m)
folium.LayerControl().add_to(m)
m.save("map.html")