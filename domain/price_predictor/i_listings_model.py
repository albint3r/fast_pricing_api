from abc import ABC, abstractmethod
import numpy


class IListingsModel(ABC):
    """ Interface for a listings model."""

    def __init__(self, m2_const: float, rooms: int, baths: int, cars: int, lat: float, long: float):
        """ Initializes a new instance of the IListingsModel class.

        Parameters:
            m2_const (float): The price constant.
            rooms (int): The number of rooms.
            baths (int): The number of bathrooms.
            cars (int): The number of parking spaces.
            lat (float): The latitude of the listing.
            long (float): The longitude of the listing. """

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
        self.img_url: str | None = None

    @abstractmethod
    def to_json(self) -> dict[str, any]:
        """ Returns the Object Class in JSON format.

        Returns:
            dict[str, float]: A dictionary containing the price.
        """
        return vars(self)

    @abstractmethod
    def to_array(self) -> numpy.array:
        """ Returns the object in Array format.

        Returns:
            dict[str, any]: A dictionary containing the object.
        """
        pass

    def __repr__(self):
        additional_info_rep: str = self.model_name if self.model_name is not None else "Listing"
        base_name_rep: str = self.additional_information_class if self.additional_information_class is not None else ""
        return f'{additional_info_rep}({base_name_rep}m2_const: {self.m2_const},' \
               f' rooms: {self.rooms}, baths: {self.baths}, cars: {self.cars}, lat: {self.lat}, long: {self.long})'
