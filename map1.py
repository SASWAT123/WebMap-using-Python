import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_elevation(elevation):
    if elevation < 1000:
        return "green"
    elif elevation >= 1000 and elevation < 3000:
        return "blue"
    else:
        return "red"

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup = str(el),fill = True, radius = 6, opacity = 0.7, color = color_elevation(el)))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data = open("World.json", "r", encoding = "utf-8-sig").read(),
style_function = lambda x : {"fillColor" : "green" if x["properties"]["POP2005"] < 1000000
else "orange" if 1000000 <= x["properties"]["POP2005"] < 2000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
