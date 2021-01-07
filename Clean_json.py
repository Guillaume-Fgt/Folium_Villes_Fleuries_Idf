import json

with open(
    "communes-dile-de-france-labellisees-villes-et-villages-fleuris-2020 - Copy.json",
    "rb",
) as f:
    data = json.load(f, encoding="utf-8")

with open(
    "communes-ile-de-france - Copy.geojson", "rb"
) as f2:  # rb pour gérer les caractères à accents
    data_2 = json.load(
        f2, encoding="utf-8"
    )  # utf8 en complément de rb pour les accents


for feature_2 in data_2["features"]:
    for feature in data["features"]:
        if (
            feature_2["properties"]["nom"]
            == feature["properties"]["commune_officielle"]
        ):
            feature_2["properties"]["fleurs"] = feature["properties"]["fleurs"]

# for feature_2 in data_2["features"]:
#     print(feature_2["properties"])
# for feature in data["features"]:
#     print(feature["properties"]["commune_officielle"], feature["properties"]["fleurs"])
with open(
    "communes-ile-de-france - Copy2.geojson", "w"
) as f:  # rb pour gérer les caractères à accents
    json.dump(data_2, f)
