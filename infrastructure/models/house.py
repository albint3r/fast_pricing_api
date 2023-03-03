import numpy as np

from domain.i_listings_model import IListingsModel


class House(IListingsModel):

    def __init__(self, m2_land: float, m2_const: float, rooms: int, baths: int, cars: int, lat: float, long: float):
        super().__init__(m2_const, rooms, baths, cars, lat, long)
        self.price_land = None
        self.m2_land = m2_land
        self.model_name = 'House'
        self.additional_information_class = f"m2_land: {self.m2_land}, "

    def to_json(self) -> dict[str, any]:
        return super().to_json()

    def to_array(self) -> np.array:
        return np.array([[self.m2_land, self.m2_const, self.rooms, self.baths, self.cars, self.lat, self.long]])
