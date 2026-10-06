from Graph import*
if __name__ == '__main__':

    connections = [
        ("USA", "CAN"),
        ("USA", "MEX"),
        ("MEX", "GTM"),
        ("MEX", "BLZ"),
        ("BLZ", "GTM"),
        ("GTM", "SLV"),
        ("GTM", "HND"),
        ("SLV", "HND"),
        ("HND", "NIC"),
        ("NIC", "CRI"),
        ("CRI", "PAN")
    ]

    Graph_object = Graph()
    Graph_object.graph_builder(connections)

    for country in Graph_object.the_nodes:
        print(country,Graph_object.the_nodes[country].get_neibours())
    print(Graph_object.shortest_route('USA' , 'PAN'))
    print(Graph_object.shortest_route("USA", "PAN"))
    print(Graph_object.shortest_route("USA", "BLZ"))
    print(Graph_object.shortest_route("USA", "CAN"))
    print(Graph_object.shortest_route("USA", "USA"))
