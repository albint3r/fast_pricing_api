import openai
from config import APIConfiguration
from domain.open_ai.i_open_ai_facade import IOPENAIFacade
from domain.models.text_completion import TextCompletion


class OPENAIFacadeImpl(IOPENAIFacade):

    def __init__(self, confing: APIConfiguration):
        self._config: APIConfiguration = confing
        openai.api_key = self._config.api_key

    def create(self, *, prompt: str) -> TextCompletion:
        response = openai.Completion.create(model=self._config.api_model,
                                            prompt=prompt,
                                            temperature=self._config.api_temperature,
                                            max_tokens=5)
        return TextCompletion.from_json(response)
