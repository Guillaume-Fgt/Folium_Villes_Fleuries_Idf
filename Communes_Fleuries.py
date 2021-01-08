import folium
import json
from branca.element import Template, MacroElement

# pour avoir le nbr par catégorie. à faire
# with open(
#     "communes-ile-de-france_fleurs_4",
# ) as f:
#     data_fleurs = json.load(f, encoding="utf-8")
# print(len(data_fleurs["features"]))

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


template = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Draggable - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  
  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>

 
<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
     
<div class='legend-title'>Nbr Fleurs Communes <br> IDF 2020 </div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style='background:#f6eff7;opacity:0.7;'></span>0</li>
    <li><span style='background:#bdc9e1;opacity:0.7;'></span>1</li>
    <li><span style='background:#67a9cf;opacity:0.7;'></span>2</li>
    <li><span style='background:#1c9099;opacity:0.7;'></span>3</li>
    <li><span style='background:#016c59;opacity:0.7;'></span>4</li>

  </ul>
</div>
</div>
 
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: center;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

macro = MacroElement()
macro._template = Template(template)

m.get_root().add_child(macro)
m.save("map.html")