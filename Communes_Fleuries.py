import folium

# charger data
communes_geo_0 = "communes-ile-de-france_fleurs_0"
communes_geo_1 = "communes-ile-de-france_fleurs_1"
communes_geo_2 = "communes-ile-de-france_fleurs_2"
communes_geo_3 = "communes-ile-de-france_fleurs_3"
communes_geo_4 = "communes-ile-de-france_fleurs_4"

# création map centrée sur Paris
m = folium.Map(
    location=[48.7, 2.3],
    zoom_start=9,
    tiles=None,
)

folium.TileLayer("CartoDB positron", name="Light Map", control=False).add_to(m)


# define the color of the Geojon data (https://leafletjs.com/reference-1.6.0.html#path-option)
colorlist = ["#f6eff7", "#bdc9e1", "#67a9cf", "#1c9099", "#016c59"]


def style_function(number):
    return lambda x: {
        "color": colorlist[number],
        "fillOpacity": 0.5,
        "weight": 0.1,
    }


highlight_function = lambda x: {
    "fillColor": "#000000",
    "color": "#000000",
    "fillOpacity": 0.50,
    "weight": 0.3,
}


def add_data_GeoJson(map, number):
    commune_data = folium.features.GeoJson(
        data="communes-ile-de-france_fleurs_" + str(number),
        style_function=style_function(number),
        highlight_function=highlight_function,
        tooltip=folium.features.GeoJsonTooltip(
            fields=["nom", "code", "fleurs"],
            aliases=["Commune: ", "Code Postal: ", "Nbr Fleurs: "],
            style=(
                "background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"
            ),
            sticky=False,
        ),
        name="Communes " + str(number) + " fleurs IDF",
    )
    map.add_child(commune_data)
    map.keep_in_front(commune_data)


commune_0 = add_data_GeoJson(m, 0)
commune_1 = add_data_GeoJson(m, 1)
commune_2 = add_data_GeoJson(m, 2)
commune_3 = add_data_GeoJson(m, 3)
commune_4 = add_data_GeoJson(m, 4)


folium.LayerControl().add_to(m)
m.save("map.html")