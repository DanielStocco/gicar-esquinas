
from OSMPythonTools.overpass import Overpass
overPass = Overpass()

# query_nodes = 'node  [!"highway"][!"traffic_signals"](-32.9816000, -68.7939000, -32.9719000, -68.7814000);out body;'
query_nodes = 'node (-32.9897, -68.9124, -32.7959, -68.7085);out body;'
# query_ways = 'way ["highway"] (-32.9710400, -68.7869200, -32.9693400, -68.7845900);out body;'
# query_ways = 'way (-32.9055000, -68.8613000, -32.8802000, -68.8105000);out body;'
nodes = overPass.query(query_nodes, timeout=100, settings={'maxsize': 2000000000})
# ways = overPass.query(query_ways)

un_nodo = nodes.toJSON()['elements'][0]

print(un_nodo)

print(un_nodo['id'] in un_nodo.values())


def busqueda_binaria(lista, id_nodo):
    """Búsqueda binaria
    Precondición: lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    """
    # Busca en toda la lista dividiéndola en segmentos y considerando
    # a la lista completa como el segmento que empieza en 0 y termina
    # en len(lista) - 1.
    izq = 0  # izq guarda el índice inicio del segmento
    der = len(lista) - 1  # der guarda el índice fin del segmento
    # un segmento es vacío cuando izq > der:
    while izq <= der:
        # el punto medio del segmento
        medio = (izq + der) / 2
        print("DEBUG:", "izq:", izq, "der:", der, "medio:", medio)
        # si el medio es igual al valor buscado, lo devuelve
        if lista[medio]['id'] == id_nodo:
            return lista[medio]
        # si el valor del punto medio es mayor que x, sigue buscando
        # en el segmento de la izquierda: [izq, medio-1], descartando la
        # derecha
        elif lista[medio] > id_nodo:
            der = medio - 1
        # sino, sigue buscando en el segmento de la derecha:
        # [medio+1, der], descartando la izquierda
        else:
            izq = medio + 1
            # si no salió del ciclo, vuelve a iterar con el nuevo segmento
    # salió del ciclo de manera no exitosa: el valor no fue encontrado
    return -1





for node in nodes.toJSON()['elements']:

    print('----------------------------------------------------------------------------')
    print(node)
    if 'tags' in node:
        print('********************************************************************************')
        print(node['tags'])
        print('********************************************************************************')
    print(node['id'])
    print(node['lat'])
    print(node['lon'])


    print('----------------------------------------------------------------------------')
#
# print("Ways: " + str(ways.countElements()))
