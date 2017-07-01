
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

# query_ways = 'way ["highway"] (-32.9055000, -68.8613000, -32.8802000, -68.8105000);out body;'
ways = overPass.query(query_ways, timeout=100, settings={'maxsize': 2000000000})
array_nodos = []
archivo.write('ID NODO | ID WAY \n')
for index, way in enumerate(ways.toJSON()['elements']):
    for node in way['nodes']:
        archivo.write(str(node) + ' | ' + str(way['id']) + '\n')
        # array_nodos.append({'node': node, 'way': way['id']})
archivo.close()
# items = 0
# for nodo in array_nodos:
#     print(nodo)
#     items += 1
#
# print(items)
