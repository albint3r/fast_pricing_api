import json
from domain.i_listings_model import IListingsModel


class Apartment(IListingsModel):

    def __init__(self, m2_land: float, rooms: int, baths: int, cars: int, lat: float, long: float):
        super().__init__(m2_land, rooms, baths, cars, lat, long)
        self.model_name = 'Apartment'

    def price_to_json(self):
        return super().price_to_json()
