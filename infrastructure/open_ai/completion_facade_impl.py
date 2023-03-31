import openai
from injector import inject

from config import APIConfiguration
from domain.open_ai.i_completion_facade import ICompletionFacade
from domain.models.completion_response import CompletionResponse


class CompletionFacadeImpl(ICompletionFacade):
    @inject
    def __init__(self, confing: APIConfiguration):
        self._config: APIConfiguration = confing
        openai.api_key = self._config.api_key

    def create(self, *, prompt: str) -> CompletionResponse:
        response = openai.Completion.create(model=self._config.api_model,
                                            prompt=prompt,
                                            temperature=0.2,
                                            max_tokens=300)
        return CompletionResponse.from_json(response)
