from fastapi import FastAPI
from domain.predict_price_facade import PredictPriceFacade
from infrastructure.models.apartment import Apartment
from infrastructure.models.house import House
from infrastructure.price_predictor.apartment_price_predictor import ApartmentPricePredictor
from infrastructure.price_predictor.house_price_predictor import HousePricePredictor

app = FastAPI()


@app.get('/house/')
async def index(m2_land: float, m2_const: float, rooms: int, baths: int, cars: int, lat: float, long: float):
    house = House(m2_land=m2_land, m2_const=m2_const, rooms=rooms, baths=baths, cars=cars, lat=lat, long=long)
    house_price_predictor = HousePricePredictor()
    facade = PredictPriceFacade(listing_model=house, trained_model=house_price_predictor)

    return facade.predict()


@app.get('/apartments/')
async def index(m2_const: float, rooms: int, baths: int, cars: int, lat: float, long: float):
    apartment = Apartment(m2_const=m2_const, rooms=rooms, baths=baths, cars=cars, lat=lat, long=long)
    apartment_price_predictor = ApartmentPricePredictor()
    facade = PredictPriceFacade(listing_model=apartment, trained_model=apartment_price_predictor)

    return facade.predict()
