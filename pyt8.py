import xml.dom.minidom
from math import sqrt

osm_file = 'osm/15.osm'
doc = xml.dom.minidom.parse(osm_file)
places = doc.getElementsByTagName('node')
data = {}
data['bus_stop'] = {}
data['school'] = {}
for place in places:
    types = place.getElementsByTagName('tag')
    f_s, f_b = 0, 0
    for t in types:
        if t.getAttribute('v') == "bus_stop":
            f_b = 1
        if t.getAttribute('v') == "school":
            f_s = 1

        if f_b and t.getAttribute('k') == 'name':
            bs = t.getAttribute('v')
            data['bus_stop'][bs] = {}
            data['bus_stop'][bs]['lat'] = place.getAttribute('lat')
            data['bus_stop'][bs]['lon'] = place.getAttribute('lon')

        if f_s and t.getAttribute('k') == 'name':
            sc = t.getAttribute('v')
            data['school'][sc] = {}
            data['school'][sc]['lat'] = place.getAttribute('lat')
            data['school'][sc]['lon'] = place.getAttribute('lon')

print(data)
print('\nAnswer:')

for key in data['school'].keys():
    dist = {}
    for k in data['bus_stop'].keys():
        x1, y1 = float(data['school'][key]['lat']), float(data['school'][key]['lon'])
        x2, y2 = float(data['bus_stop'][k]['lat']), float(data['bus_stop'][k]['lon'])
        dist[k] = sqrt((x2-x1)**2 + (y2-y1)**2)
    mn = min(dist.values())
    for t in dist.keys():
        if dist[t] == mn:
            print(f'Для {key} ближайшая остановка {t}, расстояние до неё {dist[t]}')
            break


