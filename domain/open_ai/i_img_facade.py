from abc import ABC, abstractmethod

from domain.models.img_response import ImgResponse


class IImgFacade(ABC):

    @abstractmethod
    def create(self, prompt: str, size: str) -> ImgResponse:
        pass
