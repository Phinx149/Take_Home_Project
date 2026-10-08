from Backend.Node import Node
class Graph:
    def __init__ (self):
        self.the_nodes = dict()

    def get_node_dictionary(self):
        return self.the_nodes

    def graph_builder(self , set_of_connections : list) -> None:
        # Builds a bidirectional graph dictionary
        # Input: list of connections [(country1, adjacent_country)]
        # Output: dictionary where each country maps to a Node containing its adjacent countries
        
        node_array = dict()
        occured_countries = set()
        if set_of_connections == []:
            return "for a graph to be build please enter a valid node"
        for graph_node in set_of_connections:
            first_country = graph_node[0]
            second_country = graph_node[1]

            if first_country not in occured_countries:
                occured_countries.add(first_country)
                node_array[first_country] = Node(first_country ,[second_country])
            else:
                node_array[first_country].add_neighbors(second_country)

            if second_country not in occured_countries:
                occured_countries.add(second_country)
                node_array[second_country] = Node(second_country ,[first_country])
            else:
                 node_array[second_country].add_neighbors(first_country)

        self.the_nodes = node_array
    def shortest_route(self ,Start: str,  Country_code: str) -> None:
        # Uses BFS to find the route with the fewest border crossings
        explored_set = set()
        que = []
        Route = dict()
        que.append(Start)
        while (que != []):
            country_popped = que.pop(0)
            explored_set.add(country_popped)
            if country_popped == Country_code:
    
                the_current = Country_code
                the_full_route = []
                
                # Reconstruct the route by following each country's parent
                while the_current != Start:
                    the_full_route.append(the_current)
                    the_current = Route[the_current]
                the_full_route.append(Start)
                the_full_route.reverse()
                return the_full_route
            else:
                
                possible_explore = self.the_nodes[country_popped].get_neighbors()
                for element in possible_explore:
                    if element not in explored_set:
                        que.append(element)
                        explored_set.add(element)
                        Route[element] = country_popped