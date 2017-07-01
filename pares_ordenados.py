
from OSMPythonTools.overpass import Overpass
overPass = Overpass()

# query_nodes = 'node  [!"highway"][!"traffic_signals"](-32.9816000, -68.7939000, -32.9719000, -68.7814000);out body;'
query_nodes = 'node (-32.9710400, -68.7869200, -32.9693400, -68.7845900);out body;'
query_ways = 'way ["highway"] (-32.9710400, -68.7869200, -32.9693400, -68.7845900);out body;'
# query_ways = 'way (-32.9055000, -68.8613000, -32.8802000, -68.8105000);out body;'
nodes = overPass.query(query_nodes)
ways = overPass.query(query_ways)
print("Nodos: " + str(nodes.countElements()))
print("Ways: " + str(ways.countElements()))
