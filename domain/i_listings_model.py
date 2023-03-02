import json
from abc import ABC, abstractmethod


class IListingsModel(ABC):

    def __init__(self, m2_const: float, rooms: int, baths: int, cars: int, lat: float, long: float):
        self.model_name: str | None = None
        self.additional_information_class: str | None = None
        self.price: float | None = None
        self.price_const: float | None = None
        self.m2_const = m2_const
        self.rooms = rooms
        self.baths = baths
        self.cars = cars
        self.lat = lat
        self.long = long

    @abstractmethod
    def price_to_json(self):
        return {'data': self.price if self.price is not None else 0}

    def __repr__(self):
        additional_info_rep: str = self.model_name if self.model_name is not None else "Listing"
        base_name_rep: str = self.additional_information_class if self.additional_information_class is not None else ""
        return f'{additional_info_rep}({base_name_rep}m2_const: {self.m2_const},' \
               f' rooms: {self.rooms}, baths: {self.baths}, cars: {self.cars}, lat: {self.lat}, long: {self.long})'
