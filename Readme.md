Bonjour,

j'ai utilisé des fichiers JSON et GEOJSON disponible sur data.gouv.fr pour réaliser une carte interactive en utilisant folium.

origine des données: https://www.data.gouv.fr/fr/datasets/communes-dile-de-france-labellisees-villes-et-villages-fleuris-2020/
Folium: https://python-visualization.github.io/folium/
un tuto qui m'a été très utile:https://vverde.github.io/blob/interactivechoropleth.html

Le fichier Clean_json me permet de fusionner les données venant de data.gouv.fr avec mon fichier .geojson contenant les coordonnées des communes d'ile de france.

On utilise folium.choropleth pour créer la map ensuite à partir de ces données propres.