from Backend.Graph import Graph
from Backend.Flask_app import app
import json

with open("Backend/borders.json", "r") as file:
    connections = json.load(file)
graph = Graph()
graph.graph_builder(connections)


#Testing the Graph code for the backend

def test_pan() -> None:
    route = graph.shortest_route("USA", "PAN")
    assert route == ["USA", "MEX", "GTM", "HND", "NIC", "CRI", "PAN"]


def test_blz() -> None:
    route = graph.shortest_route("USA", "BLZ")
    assert route == ["USA", "MEX", "BLZ"]


def test_can() -> None:
    route = graph.shortest_route("USA", "CAN")
    assert route == ["USA", "CAN"]


def test_usa() -> None :
    route = graph.shortest_route("USA", "USA")
    assert route == ["USA"]

#Testing  apis making malformed requestes are handles well

def test_pan_api() -> None :
    client = app.test_client()
    response = client.get("/PAN")
    assert response.status_code == 200


def test_lowercase() -> None:
    client = app.test_client()
    response = client.get("/pan")
    assert response.status_code == 200
    assert response.get_json()["destination"] == "PAN"
    assert response.get_json()['from'] == 'USA'


def test_wrong_length()-> None :
    client = app.test_client()
    response = client.get("/PA")
    assert response.status_code == 400


def test_invalid_characters() ->None:
    client = app.test_client()
    response = client.get("/P4N")
    assert response.status_code == 400


def test_country_not_supported() ->None:
    client = app.test_client()
    response = client.get("/XAZ")
    assert response.status_code == 404

def test_post_not_allowed():
    client = app.test_client()
    response = client.post("/PAN")
    assert response.status_code == 405
if __name__ == "__main__":
    test_pan()
    test_blz()
    test_can()
    test_usa()
    test_pan_api()
    test_lowercase()
    test_wrong_length()
    test_invalid_characters()
    test_country_not_supported()
    test_post_not_allowed()

    print("All tests passed")
