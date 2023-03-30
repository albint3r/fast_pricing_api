import numpy
import numpy as np

from domain.price_predictor.i_listings_model import IListingsModel


class Apartment(IListingsModel):

    def __init__(self, m2_const: float, rooms: int, baths: int, cars: int, lat: float, long: float):
        super().__init__(m2_const, rooms, baths, cars, lat, long)
        self.model_name = 'Apartment'

    def to_json(self) -> dict[str, any]:
        return super().to_json()

    def to_array(self) -> numpy.array:
        return np.array([[self.m2_const, self.rooms, self.baths, self.cars, self.lat, self.long]])
