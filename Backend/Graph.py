from Node import*
class Graph:
    def __init__ (self):
        self.the_nodes = dict()
        
    def graph_builder(self , set_of_connections : list):

        node_array = dict()
        occured_countries = set()
    
        for graph_node in set_of_connections:
            first_country = graph_node[0]
            second_country = graph_node[1]

            if first_country not in occured_countries:
                occured_countries.add(first_country)
                node_array[first_country] = Node(first_country ,[second_country])
            else:
                node_array[first_country].add_neibours(second_country)

            if second_country not in occured_countries:
                occured_countries.add(second_country)
                node_array[second_country] = Node(second_country ,[first_country])
            else:
                 node_array[second_country].add_neibours(first_country)

        self.the_nodes = node_array
    def shortest_route(self ,Start: str,  Country_code: str):
        explored_set = set()
        que = []
        Route = dict()
        que.append(Start)
        while (que != []):
            country_popped = que.pop(0)
            explored_set.add(country_popped)
            if country_popped == Country_code:
                que.append(Country_code)
                the_current = Country_code
                the_full_route = []
                
                while the_current != Start:
                    the_full_route.append(the_current)
                    the_current = Route[the_current]
                the_full_route.append(Start)
                the_full_route.reverse()
                return the_full_route
            else:
                
                possible_explore = self.the_nodes[country_popped].get_neibours()
                for element in possible_explore:
                    if element not in explored_set:
                        
                        que.append(element)
                        explored_set.add(element)
                        Route[element] = country_popped
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
