class Node:
    def __init__(self , Country_code : str  , neighbor: list):
        self.Country_code = Country_code
        self.neighbor = neighbor

    def get_country_code(self) -> str:
        # returns country code of Node
        return self.Country_code
    
    def get_neighbors(self) -> list:
        # returns neighbors of the country
        return self.neighbor

    def set_country_code(self , Country_code: str):
        # returns neighbors of the country
        self.Country_code = Country_code

    def add_neighbors(self, country_code: str) -> None:
         # adds country to neighbor
        if country_code not in self.neighbor:
            self.neighbor.append(country_code)