Bonjour,

j'ai utilisé des fichiers JSON et GEOJSON disponible sur data.gouv.fr pour réaliser une carte interactive en utilisant folium.

origine des données: https://www.data.gouv.fr/fr/datasets/communes-dile-de-france-labellisees-villes-et-villages-fleuris-2020/

Folium: https://python-visualization.github.io/folium/

un tuto qui m'a été très utile:https://vverde.github.io/blob/interactivechoropleth.html

Le fichier Clean_json me permet de créer une clé fleur pour chaque commune. Puis de séparer les niveaux (0,1,2,3,4) dans des fichiers différents.

On utilise ensuite folium dans le fichier Communes_Fleuries.py pour générer la carte avec les calques.