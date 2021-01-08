import json
import itertools

with open(
    "communes-dile-de-france-labellisees-villes-et-villages-fleuris-2020 - Copy.json",
    "rb",
) as f:
    data_fleurs = json.load(f, encoding="utf-8")

with open(
    "communes-ile-de-france.geojson", "rb"
) as f2:  # rb pour gérer les caractères à accents
    data_commune = json.load(
        f2, encoding="utf-8"
    )  # utf8 en complément de rb pour les accents

# on commence par créer une clé fleurs pour toutes les villes
for feature_commune in data_commune["features"]:
    feature_commune["properties"]["fleurs"] = 0


for feature_commune in data_commune["features"]:
    for feature_fleurs in data_fleurs["features"]:
        if (
            feature_commune["properties"]["nom"]
            == feature_fleurs["properties"]["commune_officielle"]
        ):
            feature_commune["properties"]["fleurs"] = feature_fleurs["properties"][
                "fleurs"
            ]

data_fleurie_0 = []
data_fleurie_1 = []
data_fleurie_2 = []
data_fleurie_3 = []
data_fleurie_4 = []

for feature_commune in data_commune["features"]:
    if feature_commune["properties"]["fleurs"] == 0:
        data_fleurie_0.append(data_commune["features"].index(feature_commune))
    elif feature_commune["properties"]["fleurs"] == 1:
        data_fleurie_1.append(data_commune["features"].index(feature_commune))
    elif feature_commune["properties"]["fleurs"] == 2:
        data_fleurie_2.append(data_commune["features"].index(feature_commune))
    elif feature_commune["properties"]["fleurs"] == 3:
        data_fleurie_3.append(data_commune["features"].index(feature_commune))
    elif feature_commune["properties"]["fleurs"] == 4:
        data_fleurie_4.append(data_commune["features"].index(feature_commune))

for index in sorted(
    itertools.chain(data_fleurie_0, data_fleurie_1, data_fleurie_2, data_fleurie_3),
    reverse=True,
):
    del data_commune["features"][index]


with open(
    "communes-ile-de-france_fleurs_4", "w"
) as f:  # rb pour gérer les caractères à accents
    json.dump(data_commune, f)
