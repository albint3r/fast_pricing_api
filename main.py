from fastapi import FastAPI
from domain.predict_price_facade import PredictPriceFacade
from infrastructure.models.apartment import Apartment
from infrastructure.models.house import House
from infrastructure.price_predictor.apartment_price_predictor import ApartmentPricePredictor
from infrastructure.price_predictor.house_price_predictor import HousePricePredictor

app = FastAPI()


@app.get('/house/')
async def index(m2_land: float, m2_const: float, rooms: int, baths: int, cars: int, lat: float, long: float):
    """
    Endpoint that predicts the price of a house based on its features.

    Parameters:
        m2_land (float): Total square meters of the land.
        m2_const (float): Total square meters of the house.
        rooms (int): Number of rooms.
        baths (int): Number of bathrooms.
        cars (int): Number of parking spots.
        lat (float): Latitude of the house.
        long (float): Longitude of the house.

    Returns:
        float: The predicted price of the house.
    """
    house = House(m2_land=m2_land, m2_const=m2_const, rooms=rooms, baths=baths, cars=cars, lat=lat, long=long)
    house_price_predictor = HousePricePredictor()
    facade = PredictPriceFacade(listing_model=house, trained_model=house_price_predictor)

    return facade.predict()


@app.get('/apartments/')
async def index(m2_const: float, rooms: int, baths: int, cars: int, lat: float, long: float):
    """
    Endpoint that predicts the price of an apartment based on its features.

    Parameters:
        m2_const (float): Total square meters of the apartment.
        rooms (int): Number of rooms.
        baths (int): Number of bathrooms.
        cars (int): Number of parking spots.
        lat (float): Latitude of the apartment.
        long (float): Longitude of the apartment.

    Returns:
        float: The predicted price of the apartment.
    """
    apartment = Apartment(m2_const=m2_const, rooms=rooms, baths=baths, cars=cars, lat=lat, long=long)
    apartment_price_predictor = ApartmentPricePredictor()
    facade = PredictPriceFacade(listing_model=apartment, trained_model=apartment_price_predictor)

    return facade.predict()
