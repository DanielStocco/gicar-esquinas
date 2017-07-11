
# query_nodes = 'node  [!"highway"][!"traffic_signals"](-32.9816000, -68.7939000, -32.9719000, -68.7814000);out body;'
# query_ways = 'way ["highway"] (-32.9816000, -68.7939000, -32.9719000, -68.7814000);out body;'
# query_nodes = 'node  [!"highway"][!"traffic_signals"](-32.9055000, -68.8613000, -32.8802000, -68.8105000);out body;'
# query_ways = 'way (-32.9055000, -68.8613000, -32.8802000, -68.8105000);out body;'
# nodes = overPass.query(query_nodes)
# print("Nodos: " + str(nodes.countElements()))

from OSMPythonTools.overpass import Overpass
import os
overPass = Overpass()
archivo = open('esquinas.txt', 'w')

# query_ways = 'way ["highway"] (-33.0426, -68.9063, -32.8358, -68.6948);out body;'

# query_ways = 'way ["highway"] (-33.6466, -69.1177, -32.5468, -68.1097);out body;'

#Gran mendoza
query_ways = 'way ["highway"] (-32.9897, -68.9124, -32.7959, -68.7085);out body;'
query_nodes = 'node (-32.9897, -68.9124, -32.7959, -68.7085);out body;'

# query_ways = 'way ["highway"] (-32.9055000, -68.8613000, -32.8802000, -68.8105000);out body;'
nodes = overPass.query(query_nodes, timeout=100, settings={'maxsize': 2000000000})
ways = overPass.query(query_ways, timeout=100, settings={'maxsize': 2000000000})
array_nodos = []
archivo.write('ID NODO | ID WAY | Nombre | latitud | longitud \n')
for index, way in enumerate(ways.toJSON()['elements']):
    for nd in way['nodes']:
        archivo.write(str(nd) + ' | ' + str(way['id']))
        if 'name' in way['tags']:
            archivo.write(' | ' + str(way['tags']['name']))
        else:
            archivo.write(' | Sin Nombre')
        for node in nodes.toJSON()['elements']:
            if nd in node.values():
                archivo.write(' | ' + str(node['lat']))
                archivo.write(' | ' + str(node['lon']))
                break
        archivo.write('\n')

        # array_nodos.append({'node': node, 'way': way['id']})
archivo.close()
# items = 0
# for nodo in array_nodos:
#     print(nodo)
#     items += 1
#
# print(items)
