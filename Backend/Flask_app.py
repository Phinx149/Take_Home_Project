from Backend.Graph import Graph


from flask import Flask ,jsonify

app = Flask(__name__)

Start_country = 'USA'

connections = [("USA", "CAN"),("USA", "MEX"),("MEX", "GTM"),("MEX", "BLZ"),("BLZ", "GTM"),("GTM", "SLV"),("GTM", "HND"),("SLV", "HND"),("HND", "NIC"),("NIC", "CRI"),("CRI", "PAN")]

Graph_object = Graph()
Graph_object.graph_builder(connections)
available_country = Graph_object.get_node_dictionary()

@app.route('/<Destination>')
def Give_Shortest_Route(Destination: str ):
    Start_country = 'USA'
    connections = [("USA", "CAN"),("USA", "MEX"),("MEX", "GTM"),("MEX", "BLZ"),("BLZ", "GTM"),("GTM", "SLV"),("GTM", "HND"),("SLV", "HND"),("HND", "NIC"),("NIC", "CRI"),("CRI", "PAN")]
    Graph_object = Graph()
    Graph_object.graph_builder(connections)

    error_message = []
    available_country = Graph_object.get_node_dictionary()
    Destination = Destination.upper().strip("")
    
    if len(Destination) != 3:
        error_message.append("error : Country need three letter word")
    if Destination.isalpha() == False:
        error_message.append("error : country needs to be composed of only alphabhetic characters")
    if error_message != []:
        return jsonify(error_message) , 400
    if Destination not in available_country:
        return jsonify({'error' : "Country code is not supported. May be supported in future updates"}) , 404
        
    return jsonify({"Route" :Graph_object.shortest_route(Start_country , Destination) , "from" : Start_country, "destination" : Destination}), 200
if __name__ == '__main__':
    app.run(debug= True)