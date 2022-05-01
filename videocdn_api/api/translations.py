from videocdn_api.models.responses import TranslationsResponse


class TranslationsApi:
    def __init__(self, api):
        self.api = api

    async def get(self, **params) -> TranslationsResponse:
        """
        Has no additional parameters at the time of writing/updating this library
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return TranslationsResponse(**(await self.api.make_get_request(self, 'translations', params)))
