import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

#FUNCTION TO CHANGE MARKER BASED ON ELEVATION NUMBERS
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<= elevation < 3000:
        return "blue"
    else:
        return "red"

map = folium.Map(location=[38,-99], zoom_start=5, tiles = "Stamen Terrain")

feat_group1 = folium.FeatureGroup(name="Volcanoes")

#WHEN GOING THROUGH 2 LISTS, USE THE "ZIP FUNCTION"
for lt, ln, el, name in zip (lat, lon, elev, name):
    feat_group1.add_child(folium.CircleMarker(location=[lt, ln], radius = 9, popup=str(el) +" Meters", fill_color = color_producer(el), color = "white", fill_opacity=0.7))


#AADING POPULATION BASED ON COLORS
feat_group2 = folium.FeatureGroup(name="Population")

feat_group2.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x ['properties'] ['POP2005'] < 10000000 else 'orange' if 10000000 <= x ['properties']['POP2005'] < 20000000 else 'purple'}))


map.add_child(feat_group1)
map.add_child(feat_group2)
map.add_child(folium.LayerControl())

map.save("Map1.html")
