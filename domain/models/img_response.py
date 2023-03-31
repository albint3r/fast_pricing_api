from dataclasses import dataclass

from domain.models._json_serialize import JsonSerialize


@dataclass
class ImgResponse(JsonSerialize):
    created: int
    data: list[dict]
