import openai
from injector import inject

from config import APIConfiguration
from domain.models.img_response import ImgResponse
from domain.open_ai.i_img_facade import IImgFacade


class ImgFacadeImpl(IImgFacade):
    @inject
    def __init__(self, confing: APIConfiguration):
        self._config: APIConfiguration = confing
        openai.api_key = self._config.api_key

    def create(self, *, prompt: str, size: str = '512x512') -> ImgResponse:
        response = openai.Image.create(prompt=prompt, n=1, size=size)
        return ImgResponse.from_json(response)
