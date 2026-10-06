class Node:
    def __init__(self , Country_code : str  , neibour: list):
        self.Country_code = Country_code
        self.neibour = neibour


    def get_country_code(self) -> str:
        return self.Country_code
    
    def get_neibours(self) -> list:
        return self.neibour

    def set_country_code(self , Country_code: str):
        self.Country_code = Country_code



    def add_neibours(self, country_code: str) -> None: 
        if country_code not in self.neibour:
            self.neibour.append(country_code)
