from fastapi import FastAPI

from data.models.house import House

app = FastAPI()


@app.get('/house/{m2_land}-{m2_const}-{rooms}-{baths}-{cars}-{lat}-{long}')
async def index(m2_land: float, m2_const: float, rooms: int, baths: int, cars: int, lat: float, long: float):
    house = House(**{
        'm2_land': m2_land,
        'm2_const': m2_const,
        'rooms': rooms,
        'baths': baths,
        'cars': cars,
        'lat': lat,
        'long': long,
    })
    return house.price_to_json()
